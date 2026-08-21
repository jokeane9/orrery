# Is branch reconciliation a product?

**Research + decision record.** Prompted by finding 28 unmerged branches in
`wp-diagnostic` and 15 in `mission-control-desktop`, generated solo by agent
workflows in under three weeks.

*2026-08-21 · one commissioned probe · load-bearing claims verified by hand against
papers, primary docs and the GitHub API.*

---

## PM summary

We asked whether "untangle the branches agents leave behind" is a product.

**Answer: not yet, and probably not by us — but the ground under it is genuinely
moving.**

The strongest finding argues against building. **Our branches are 1–3 commits
each.** On the classic discipline metric — keep branches small — the workflow is
already exemplary. What failed is *merge cadence*, not branch size. Six
`sessions-*` branches were created the same day touching the same three files;
merging each the day it was written would have produced near-zero conflict. At the
published median of **11 minutes per conflict**, clearing every conflicting branch
we have is about **two hours of work**. An annoying afternoon, not a market.

**Microsoft already built this and never shipped it.** ConE did pre-PR cross-branch
conflict detection across 234 repos, assessed 26,000 PRs, and 70% of developers who
saw its recommendations rated them useful. Never released, never open-sourced. The
public equivalent — GitHub's own OSPO `pr-conflict-detector` — has **3 stars and 1
fork**, verified. That number is the market.

**And the prediction premise is academically weak.** Leßenich et al. tested the
seven intuitive conflict predictors across 21,488 merge scenarios and **rejected all
seven**. "Files changed by both branches" correlates at 0.40. Our repo matched the
intuition; the literature says it doesn't generalise.

**But the counter-evidence is real and new.** Agent PRs conflict at **27.67%**
across 142,652 measured PRs. **79.4% of agent PRs are open concurrently with another
agent PR**, and cross-agent pairs conflict at **41.7%** versus 19.8% same-agent. A
CMU difference-in-differences study isolates agents as causing **+36.25% commits,
+76.59% lines added**. CircleCI telemetry shows feature-branch activity up 15% while
main-branch throughput fell 7%, with main-branch success at a five-year low.

So this is **both** a self-inflicted workflow problem **and** an early instance of a
structural shift. Holding only one of those would be wrong.

## Recommendations

**Do**

1. **Fix cadence before building anything.** Land branches the day they're written,
   or stack them. Removes most of the pain at zero engineering cost. DORA's guidance
   is ≤3 active branches; we have 15–28.
2. **Keep the collision query.** The two-command sweep that found seven branches
   fighting over one file is genuinely useful. Ship it as `orrery collisions` — a
   CLI query, not a product.
3. **Watch `Ataraxy-Labs/weave`** (1,256★ / 40 forks, 188 points on HN) — the only
   project here with real traction. If it grows into N-branch reasoning, the gap
   closes.

**Don't**

4. **Don't build a conflict *predictor*.** The literature rejects the premise, and
   ConE — the one that worked — was tuned so hard it flagged only 3% of PRs.
5. **Don't promise agent auto-resolution.** The best LLMs correctly resolve **under
   60%** of merge conflicts. See §05.

**Watch**

6. If cross-agent conflict rates keep climbing and someone publishes branch-count
   telemetry, revisit. Right now **nobody measures branch counts at all** — there is
   no population baseline for our 28.

---

## 01 · What our own repos showed

| | `wp-diagnostic` | `mission-control-desktop` |
|---|---|---|
| Unmerged branches | 28 | 15 |
| Conflicting against main | 6 of 9 sampled | **11 of 15 (73%)** |
| Commits per branch | 1–3 | 1–3 |
| Worst collision | `pm/KNOWN-ISSUES.md` — 7 branches | `generate.py` — 9 branches |

**Every worktree was clean** — 0 dirty files across all six under
`.claude/worktrees/`, plus six stale registry entries pointing at deleted
directories. The worktree thesis in [`STRANDED-WORKTREES.md`](STRANDED-WORKTREES.md)
does not reproduce here: **the branches are the mess, not the worktrees.**

**The conflicts are staleness, not disagreement.** Inspecting
`fleet-phase1/report-endpoint` — one commit, 12 files flagged, 4 with real markers,
16 hunks — every hunk has the same shape: main gained the Phase 3 digest columns and
a scope column; the branch still carries the older schema. Nothing argues with
anything. The branch is simply behind.

## 02 · The counter-case, which is strong

1. **Branch size is already right.** 1–3 commits each. The classic remedy is
   followed; deferred merging is the failure.
2. **The cost is small.** Median resolution **11 minutes** (Vale et al., 81,005 merge
   scenarios, 66 projects; Q1 2.5 min, Q3 1.77 hours). ~2 hours for our whole
   backlog.
3. **Existing remedies would have worked.** Merge-on-green, a merge queue, or stacked
   PRs prevent this exact situation.
4. **Prediction is a rejected premise.** Leßenich et al. (*Automated Software
   Engineering* 2018), 21,488 merge scenarios, 163 projects: all 7 developer-named
   indicators rejected. Commits 0.16, commit density 0.13, files changed by both
   0.40, lines changed 0.43.
5. **Base rates are ordinary.** Conflicts occur in 10–20% of merges — Ghiotto et al.
   (IEEE TSE 2018, 2,731 projects), Leßenich et al. (11.0%), Brindescu et al.
   (EMSE 2019, ~1 in 5).

## 03 · The evidence that something is genuinely changing

- **AgenticFlict** (arXiv 2604.03551, peer-reviewed AIware '26): 142,652 agentic PRs
  across 59,412 repos; 107,026 merge-simulated; **29,609 conflicted = 27.67%**; mean
  **540 conflict lines per PR**. By agent: Copilot 15.24% · Cursor 19.75% · Devin
  22.85% · **Claude Code 25.93%** · Codex 31.85%.
  ⚠️ The authors state there is **no human-authored baseline** — do not compare
  27.67% against the ~20% human figure.
- **Concurrency** (arXiv 2607.04697): **79.4% of agent PRs are co-active** with
  another agent PR. Merge-replay of 716 pairs — intra-agent **19.8%**, **cross-agent
  41.7%**. (Cross-agent N is only 115 pairs.)
- **Causal volume** (Agarwal, He, Vasilescu, CMU, MSR '26): staggered
  difference-in-differences, 401 agent-first repos vs 606 controls — **+36.25%
  commits, +76.59% lines added**, versus +3.06% / −6.34% for IDE-assistant-first
  repos. Isolates agents specifically, not AI assistance generally.
- **CircleCI** (28,738,317 workflows): median team **feature branches +15%, main
  branch −7%**; main-branch success **70.8%, lowest in 5+ years**. Their reading:
  *"new difficulties reviewing, validating, and promoting AI-generated changes into
  shared code."*
- **Batch size up at three vendors independently**: DX median PR 44 → 72 lines;
  Swarmia batch size roughly doubled; LinearB — AI PRs wait 4.6× longer for pickup,
  agentic 5.3×.

## 04 · What exists, and the gap

**Two buckets with almost nothing between them.**

**Serialize** — GitHub merge queue, Mergify, Graphite, Aviator, bors. These don't
reconcile, they **eject**: GitHub's docs say a PR with base-branch conflicts *"will
be removed from the queue."* Git itself refuses — the octopus strategy *"refuses to
do a complex merge that needs manual resolution."*
Health check: `bors-ng` **archived** (1,530★, dead since 2024); `Mergify` last pushed
2023, engine now closed-source.

**Resolve one conflict** — `devlint/GitWand` 164★/7f, and a graveyard beneath it.

| Capability | State |
|---|---|
| Pre-PR cross-branch detection | Solved in research twice (Crystal FSE 2011, WeCode ICSE 2012). Shipped **once, internally** — Microsoft **ConE**: 234 repos, 26,000 PRs assessed, **775 recommendations (~3% of PRs)**, 70% rated useful. **Never released.** OSS equivalent `github-community-projects/pr-conflict-detector`: **3★ / 1 fork** ✅ verified |
| Conflict-minimising merge **order** | Essentially nonexistent. Cassandra (ICSE 2013) never left academia. Graphite reorders for throughput, not collision |
| Reconcile N in-flight branches | `clash-sh/clash` **63★ / 1f** ✅ · `AyushPramanik/Mesh` 8★ · `grove` 13★ · `DriftWatch` 0★ |

**The one real signal:** **`Ataraxy-Labs/weave` — 1,256★ / 40 forks** ✅ verified,
actively pushed. An entity-level merge driver: *"Resolves false conflicts git invents
when independent agents edit the same file."* **188 points on HN.** It validates the
pain — but it improves *one* merge. It does not reason across N branches or
recommend order.

**Meanwhile the orchestration category is enormous and stops at isolation** —
vibe-kanban 27,878★ (stale), agent-orchestrator 9,698★, claude-squad 8,348★,
worktrunk 6,569★, container-use 4,014★. Every one hands each agent a worktree and
stops there.

## 05 · Correction to an earlier claim

Mid-session I said these staleness conflicts were something "an agent does in
minutes." That over-generalised.

**Merge-Bench** (arXiv 2605.25890, 7,938 real conflict hunks from 1,439 repos) —
verified verbatim: *"The best models correctly resolve less than 60% of merge
conflicts."* And Shen et al. (arXiv 2102.11307, 204 hand-analysed conflicts): **79%
of compiling conflicts and 75% of semantic conflicts go undetected by any tool**, let
alone resolved.

The narrower claim survives: **textual staleness conflicts are the tractable
subset** — tools can suggest resolutions for 92% of textual conflicts and 86% are
theoretically auto-resolvable. Ours are that kind. But "an agent resolves merge
conflicts" as a general promise is not supported.

## 06 · Honest empties

- **Nobody measures branch counts.** Every dataset counts PRs, commits or workflows.
  No baseline exists for our 28.
- **"Branch sprawl" is an unclaimed term** — zero exact-phrase hits on Hacker News,
  no paper, no first-party engineering blog. Same naming problem as stranded
  worktrees: unsearchable, therefore unsellable.
- **No credible figure for the share of developer time lost to conflicts.** Every
  "X hours per week" claim dead-ends in SEO content.
- **Practitioners frame this as review bandwidth, not branches.** Simon Willison and
  Armin Ronacher both name human review as the binding constraint on parallel agents;
  Willison doesn't use worktrees at all.

---

*Methodology note: this topic is severely SEO-contaminated. The circulating "PR volume
up 98% per developer, attributed to Faros" is LinearB's 95.7%, mangled. The commonly
quoted CircleCI "59%" is average throughput across all branches, not feature branches.
Verify before citing anything in this space.*
