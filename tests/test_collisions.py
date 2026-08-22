#!/usr/bin/env python3
"""Collisions view tests — patch-id triage, mergeability, dedupe, guards.

The load-bearing one is `test_squash_merged_reads_as_landed`. Ancestry-based
checks (`--no-merged`, `git branch --merged`) call a squash-merged branch
unmerged forever, because squashing never makes its commits ancestors of the
trunk. Measured on the maintainer's own repos, that mislabelled a THIRD of the
branches — so if this test ever goes green for the wrong reason, the view starts
telling people to reconcile work that already shipped.

Builds real git repos in a temp dir: every verdict here is git reachability and
patch-id arithmetic, so faking the git layer would test nothing.
Stdlib only; run: python tests/test_collisions.py  (exits non-zero on failure)."""
import os, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import views as V


def git(repo, *args):
    return subprocess.run(["git", "-C", repo] + list(args),
                          capture_output=True, text=True).stdout.strip()


def mkrepo(base, name):
    d = os.path.join(base, name)
    os.makedirs(d, exist_ok=True)
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@example.com")
    git(d, "config", "user.name", "T")
    write(d, "README.md", "# hi\n")
    git(d, "add", "-A")
    git(d, "commit", "-qm", "init")
    return d


def write(d, fname, body):
    path = os.path.join(d, fname)
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(fname) else None
    open(path, "w").write(body)


def commit(d, fname, body, msg="work"):
    write(d, fname, body)
    git(d, "add", "-A")
    git(d, "commit", "-qm", msg)


def branch_of(recs, name):
    for b in recs["branches"]:
        if b["name"] == name:
            return b
    raise AssertionError(f"{name} missing from {[b['name'] for b in recs['branches']]}")


def only(base, d, name="r"):
    out = V.collect_collisions([(name, d)])
    assert out, "expected one repo record"
    return out[0]


# --------------------------------------------------------------------------- #
def test_squash_merged_reads_as_landed(tmp):
    """The whole reason this view exists. A squash-merged branch is NOT an
    ancestor of main, so ancestry says unmerged — patch-id must say landed."""
    d = mkrepo(tmp, "squash")
    git(d, "checkout", "-q", "-b", "feature")
    commit(d, "feat.txt", "one\n", "add feat")
    git(d, "checkout", "-q", "main")
    git(d, "merge", "-q", "--squash", "feature")
    git(d, "commit", "-qm", "squashed feature")

    # Ancestry disagrees with reality — this is the trap being guarded.
    assert "feature" in git(d, "for-each-ref", "--format=%(refname:short)",
                            "--no-merged", "main", "refs/heads"), \
        "precondition: ancestry should call the squashed branch unmerged"

    rec = only(tmp, d)
    assert branch_of(rec, "feature")["verdict"] == "landed", \
        "patch-id triage must see the squashed branch as already in main"
    assert rec["landed"] == 1


def test_real_work_is_not_landed(tmp):
    d = mkrepo(tmp, "pending")
    git(d, "checkout", "-q", "-b", "wip")
    commit(d, "new.txt", "novel\n", "genuinely new")
    git(d, "checkout", "-q", "main")

    b = branch_of(only(tmp, d), "wip")
    assert b["verdict"] == "clean", f"expected clean, got {b['verdict']}"
    assert b["novel"] == 1 and b["commits"] == 1


def test_conflict_is_detected_and_files_named(tmp):
    d = mkrepo(tmp, "conflict")
    git(d, "checkout", "-q", "-b", "theirs")
    commit(d, "shared.txt", "their side\n")
    git(d, "checkout", "-q", "main")
    commit(d, "shared.txt", "our side\n")

    b = branch_of(only(tmp, d), "theirs")
    assert b["verdict"] == "conflict", f"expected conflict, got {b['verdict']}"
    assert "shared.txt" in b["conflict_files"]


def test_collisions_need_two_pending_branches(tmp):
    """A file is only a collision when two branches that still have to LAND
    both touch it. Already-landed branches must not inflate the count."""
    d = mkrepo(tmp, "collide")
    for name in ("a", "b"):
        git(d, "checkout", "-q", "-b", name, "main")
        commit(d, "hot.txt", f"{name}\n")
    git(d, "checkout", "-q", "main")

    rec = only(tmp, d)
    hot = [c for c in rec["collisions"] if c["file"] == "hot.txt"]
    assert hot and sorted(hot[0]["branches"]) == ["a", "b"], \
        f"expected a+b colliding on hot.txt, got {rec['collisions']}"

    # A third branch that's already landed must not join the collision.
    git(d, "checkout", "-q", "-b", "c", "main")
    commit(d, "hot.txt", "c\n")
    git(d, "checkout", "-q", "main")
    git(d, "merge", "-q", "--squash", "c")
    git(d, "commit", "-qm", "squash c")
    rec = only(tmp, d)
    assert branch_of(rec, "c")["verdict"] == "landed"
    hot = [c for c in rec["collisions"] if c["file"] == "hot.txt"]
    assert "c" not in (hot[0]["branches"] if hot else []), \
        "a landed branch must not count toward a live collision"


def test_dedupes_by_tip_not_name(tmp):
    """Two remotes carrying the same branch is ONE branch. Counting it twice
    doubles every collision number it appears in."""
    d = mkrepo(tmp, "dupes")
    git(d, "checkout", "-q", "-b", "shared")
    commit(d, "x.txt", "x\n")
    git(d, "checkout", "-q", "main")
    sha = git(d, "rev-parse", "shared")
    for remote in ("origin", "upstream"):
        git(d, "update-ref", f"refs/remotes/{remote}/shared", sha)

    cands = V._branch_candidates(d, "main")
    names = [n for n, _, _ in cands]
    assert names.count("shared") == 1, f"local should win, got {names}"
    assert not any(n.endswith("/shared") for n in names), \
        f"remote duplicates of the same tip must collapse, got {names}"


def test_base_branch_is_never_a_candidate(tmp):
    d = mkrepo(tmp, "basecheck")
    assert not V._branch_candidates(d, "main")


def test_fork_sized_repo_is_skipped_out_loud(tmp):
    """A mirror gets skipped for cost — but it must SAY so. A silent cap would
    report 'nothing outstanding' for a repo that was never examined."""
    d = mkrepo(tmp, "mirror")
    sha = git(d, "rev-parse", "HEAD")
    for i in range(V._COLL_MAX_REFS + 2):
        git(d, "update-ref", f"refs/remotes/origin/b{i}", sha)
    # Distinct tips, or the dedupe would collapse them before the guard fires.
    git(d, "checkout", "-q", "-b", "seed")
    for i in range(V._COLL_MAX_REFS + 2):
        commit(d, f"f{i}.txt", f"{i}\n")
        git(d, "update-ref", f"refs/remotes/origin/b{i}", git(d, "rev-parse", "HEAD"))
    git(d, "checkout", "-q", "main")

    rec = only(tmp, d)
    assert rec["skipped"], "an over-sized repo must report why it was skipped"
    assert "fork or mirror" in rec["skipped"]
    assert rec["branches"] == []


def test_ahead_behind_orientation(tmp):
    """Getting ahead/behind backwards would invert every 'N behind' in the
    output, which is the number that tells you how stale a branch is."""
    d = mkrepo(tmp, "orient")
    git(d, "checkout", "-q", "-b", "side")
    commit(d, "side.txt", "s\n")
    git(d, "checkout", "-q", "main")
    commit(d, "main1.txt", "m\n")
    commit(d, "main2.txt", "m\n")

    ahead, behind = V._ahead_behind(d, "main", "side")
    assert (ahead, behind) == (1, 2), f"expected side +1/-2, got +{ahead}/-{behind}"


def test_clean_repo_yields_no_record(tmp):
    d = mkrepo(tmp, "clean")
    assert V.collect_collisions([("clean", d)]) == []


# --------------------------------------------------------------------------- #
def main():
    tmp = tempfile.mkdtemp(prefix="orrery-collisions-")
    failed = 0
    try:
        for name, fn in sorted(globals().items()):
            if not name.startswith("test_") or not callable(fn):
                continue
            try:
                fn(tmp)
                print(f"  ok   {name}")
            except AssertionError as e:
                failed += 1
                print(f"  FAIL {name}: {e}")
            except Exception as e:                    # noqa: BLE001 — report, don't mask
                failed += 1
                print(f"  ERR  {name}: {type(e).__name__}: {e}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("FAILED" if failed else "all collisions tests passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
