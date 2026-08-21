# Is stranded-worktree cleanup a product?

**Decision record.** The gap is real, verified from Anthropic's own docs, and
structurally unoccupied in one specific respect. **It is probably not a business.**
Keep the Worktrees view because it serves the maintainer; don't build a company on
it.

*2026-08-20 · one commissioned probe plus a code-level audit of ~18 orchestrators ·
every load-bearing claim verified by hand against primary docs or the GitHub API.*

---

## 01 · The mechanism — the dangerous population is by design

From [Claude Code's own worktrees doc](https://code.claude.com/docs/en/worktrees),
verified verbatim:

> "The sweep skips a worktree that still holds work: changed or untracked files, or
> unpushed commits. **It never removes worktrees you create with `--worktree`.**"

> "Non-interactive runs with `-p` have no exit prompt, so Claude doesn't clean up
> their worktrees."

> "Claude Code leaves the refused directory in place, since it may hold work."

So the automatic sweep **deletes the safe worktrees and permanently retains the
dangerous ones.** That is correct behaviour — you never want an automated process
force-deleting uncommitted work.

**But there is no surface to review what it kept.** No `/worktree` command, no
`--cleanup` flag, no subcommand. The documented remedy is raw git:
`git worktree remove --force`.

The six ghost worktrees found on 2026-07-16, up to 68 days old, were not a bug.
They are the documented, intended outcome of everyone behaving correctly.

**And the population is growing by design:** *"In the desktop app, every new session
gets its own worktree automatically."* Every session, every desktop user.

Anthropic has patched worktree leaks repeatedly (changelog entries at 2.1.76,
2.1.98, 2.1.105, 2.1.143, 2.1.157, 2.1.187, 2.1.210, 2.1.211) — every one scoped to
*agent/subagent/background* worktrees, none adding a review surface.

## 02 · Who is exposed

Bounds the addressable population, and it's smaller than "everyone using AI."

| Agent | Creates local worktrees? |
|---|---|
| **Claude Code** | **Yes** — `.claude/worktrees/`; desktop auto-creates per session |
| **Gemini CLI** | **Yes** — `.gemini/worktrees/` |
| **Copilot CLI** | **Yes** — `/worktree`, `--worktree` |
| **Codex** | No — worktree-*aware*, not creating |
| **Aider** | No |
| **Cursor** | **No** locally — cloud-agent feature only (verified in `multitool-sessions-plan.md`) |
| **Amp** | Unverified — no public repo |

**Cursor was doing ~$2B annualized and never produces this problem.** The affected
set is Claude Code / Gemini CLI / Copilot CLI users running long or parallel
sessions.

**It is not a team problem.** A worktree is a folder on local disk. A teammate
cannot see it, cannot be blocked by it, and is unaffected when you strand one. No
shared state, nothing propagates. This is single-player by construction — which
rules out any "our team keeps hitting this" pitch.

### The cross-tool claim needs narrowing

A verified survey (n=396, Apr–May 2026) puts **98% of engineering orgs on AI coding
assistants, averaging 2.4 tools simultaneously.** The aggregation problem is real
and no vendor will ever solve it — Cursor won't show you Claude Code's work. That
remains the one structurally defensible position.

**But Orrery's cross-tool coverage is thinner than the pitch implies**, and
`multitool-sessions-plan.md` already established why: git records who you are,
never which agent typed the commit. So Work Log and Worktrees are tool-*agnostic*,
not tool-aware. **Sessions is the only genuinely cross-tool view.**

And the two most differentiated things in the app are Claude-only by data
availability:

- **Worktrees** — Cursor creates none locally. The strongest view covers one vendor.
- **Token charts** — Cursor's `usageData` is blank on every session.

**The asymmetry to plan around:** the *cost* of cross-tool scales with vendor
count, but the *value* doesn't — because the intersection of what all vendors
expose shrinks as you add them. Claude Code gives repo, branch, files, tools,
tokens, worktrees, timing, messages. Cursor gives repo, branch, files, tools,
timing, messages — no tokens, no PRs, no worktrees. The shared set is already down
to the least informative fields; a third vendor shrinks it again. Meanwhile the
maintenance is permanent: Cursor's schema has no contract and renames fields
silently, Claude Code's JSONL is documented as unstable/internal, and Cursor now
sits inside SpaceX.

**Cross-tool aggregation converges on the lowest common denominator.** Claim it
where it's true — Sessions and the per-repo timeline — and don't stretch it to
cover the rest. The headline is git-anchored; cross-tool is one view on top.

## 03 · The competitive audit

~18 tools examined, most at source level. Star/fork counts pulled from the GitHub
API on 2026-08-20.

### The ones that matter

| Tool | ★ / forks | Dirty guard | Sees *foreign* worktrees |
|---|---|---|---|
| **container-use** (Dagger) | 4,014 / 201 | Bare `os.RemoveAll` (mitigated by auto-commit) | No |
| **spec-kitty** | 1,526 / 147 | At reuse, not at delete | Partial — as a do-not-delete set |
| **jean** | 1,190 / 152 | **None** | No — `list_worktrees` is dead code |
| **parallel-code** | 982 / 127 | Uncommitted *and* unmerged | **Yes — adopts them, never deletes** |
| **bernstein** | 941 / 123 | Strongest: salvage + `refs/graveyard/` + preserve-on-doubt | No |
| **codexia** | 892 / 97 | Yes on auto paths, none on manual UI delete | No |
| **hive** | 462 / 55 | Yes, renderer-side with file list | Yes |
| **wmux** | 352 / 60 | Refuses dirty, fails closed, 4-state orphan classifier | No |
| **operator-oss** | 200 / 29 | `worktreePruneSafety()` + explicit `discardChanges` ack | No |

Also audited: worktrunk (6,557/234 — best-in-class, reads git's registry, hooks
Claude Code's `WorktreeCreate`), Nimbalyst, Pane, dmux, Paneflow, gwq, phantom,
branchlet, Crystal (deprecated), uzi (abandoned).

### 🔴 Vibe Kanban is dead — and it's the headline

**27,868★ / 2,978 forks. Last push 2026-04-24. Sunset.** Stated reason:

> "the vast majority are free users and we couldn't find a business model that we
> could get excited about"

A YC-backed team, with distribution most products never achieve, in exactly this
category, could not monetise it. Its own top worktree issue — *"Configurable
automatic cleanup of worktrees,"* 19 reactions — sat open eleven months and never
shipped.

*(Note: Vibe Kanban is itself the pivoted remains of bloop AI, a YC COBOL→Java
migration startup. Two failed theses, one team.)*

### Some of these tools generate the problem

**`jean` (1,190★)** has no `git status` check anywhere on its delete path; its close
dialog carries no git state at all — no file count, no warning. Default removal
behaviour is `delete`, not archive. And its orphan logic runs backwards: it prunes
DB rows whose directory is gone, but never scans disk for worktrees missing from
the DB. A crash between `git worktree add` and the DB write leaves a worktree
**permanently invisible to the tool that created it.**

## 04 · What is actually unoccupied

Stated precisely — an earlier draft of this analysis overclaimed here and was
corrected.

**Occupied:** *detection* of foreign worktrees. `parallel-code` runs
`git worktree list --porcelain`, filters out the main checkout and what it already
tracks, and offers the rest — including `.claude/worktrees/` — for adoption, then
flags them `externalWorktree: true` and never git-cleans them. `hive` also
enumerates and reconciles.

**Unoccupied, verified across all ~18:**

1. **Triage of foreign worktrees.** parallel-code detects and *adopts*. It doesn't
   rank them, doesn't say which are safe to remove, doesn't say which hold
   unrecoverable work. Detection is not a verdict.
2. **Reachability-based verdicts.** Nobody computes whether HEAD is reachable from
   *any* branch. Every safety check in the category is one of two things:
   `git status --porcelain`, or a comparison against a **named** branch. bernstein
   gets closest (`merge-base --is-ancestor HEAD main` with upstream fallback,
   undecidable treated as unsaved) — still branch-anchored. Our case has no branch
   to anchor to.
3. **Read-only posture.** Every tool here is built to act — create, adopt, remove,
   archive. Not one simply reports and leaves the decision alone, which is exactly
   what the dangerous population requires.

⚠️ **Research hygiene note:** an earlier pass reported that `bernstein` reads git's
registry. A source-level read found its *docstring* claims that while the
implementation is a filesystem scan of its own directory. Docstrings are not
behaviour.

## 05 · Demand is quiet — and this is the decisive input

- **No name exists.** "stranded worktree," "zombie worktree," "ghost worktree,"
  "worktree sprawl," "worktree leak" — **0 usage each** on HN and in web search.
  Nobody can search for a problem that has no name.
- **Hacker News: effectively zero.** "git worktree" → 467 hits. "worktree cleanup"
  → **2**. "stale worktrees" → **0**. HN loves worktrees as a topic (156 pts on a
  parallelization post) and has never once complained about cleanup.
- **Engagement ceiling is 30 reactions** —
  [anthropics/claude-code#26725](https://github.com/anthropics/claude-code/issues/26725)
  "Stale worktrees are never cleaned up," open since 2026-02-18. Field reports
  in-thread: 13 worktrees / 13.8 GB in 11 days. In the same repo, worktree
  *ergonomics* issues hit 108, 90, 84, 80, 61. **Cleanup is a third-tier concern
  inside a first-tier topic.**
- **The market pays for spawning, not reclaiming.** Creation tools: 234 / 214 / 138
  forks. Dedicated cleaners: 8★/0 forks, 3★, 2★, 1★.
- One real independent write-up:
  [brtkwr.com, 2026-03-06](https://brtkwr.com/posts/2026-03-06-bulk-cleaning-stale-git-worktrees/)
  — 256 worktrees → 28 across 46 repos, ~27 GB, explicitly blamed on AI agents.

## 06 · Verdict

**Real, verified, partially unoccupied — and not a business.**

Keep the Worktrees view. It earns its place in daily use, it was built from genuine
pain, and it is one of the few things here nobody else does well. If it's ever
extended, the differentiators are reachability verdicts and read-only triage of
*foreign* worktrees — both confirmed unclaimed.

Do not build a company on it. Demand tops out at 30 reactions, the problem is
unnamed and therefore unsearchable, dedicated cleaners attract zero forks, and the
category's flagship shut down with 27,868 stars because free users don't convert.

## 07 · What would change this

1. **The problem gets a name and the name spreads.** Naming may be a prerequisite
   to anyone recognising they have it.
2. **Anthropic ships a review surface** (`/worktree list`, a cleanup command). That
   closes the gap entirely — and given eight changelog entries in two years of
   patching around it, it's plausible.
3. **worktrunk absorbs it.** It already reads git's registry rather than a private
   DB, already sweeps a trash dir on a 24h timer, and already hooks Claude Code's
   `WorktreeCreate`. "Scan for foreign worktrees and rank them" is a plausible
   increment for them, not a rewrite.

---

*Confidence: **high** on the Claude Code mechanics (primary docs, quoted verbatim),
the Vibe Kanban sunset, and every star/fork figure (API-verified individually).
**Medium-high** on "no tool computes reachability" — broad source search, not
exhaustive. **High** on the quiet-demand finding: multiple independent probes all
returned near-empty.*
