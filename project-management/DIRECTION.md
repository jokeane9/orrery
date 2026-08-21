# Where Orrery goes next

**Forward-looking, not a decision record.** Everything else written this week was a
*no* — multiplayer, team servers, compliance, worktree-cleanup-as-a-business. Those
were four specific bets, not a verdict on the space. This file is the other half:
what the same research says is worth building.

*2026-08-21 · read with [`ROADMAP.md`](ROADMAP.md) for ordered work.*

---

## The filter

Four tests, each earned from something that failed this week. A candidate feature
should pass all four.

| Test | Why | What failed it |
|---|---|---|
| **Git- or filesystem-anchored** | Vendor session formats churn — Claude Code's JSONL is documented unstable, Cursor's has no contract. Git doesn't churn. | Team server, git-as-transport, agent-to-agent handoff |
| **Only visible from where you stand** | If it's legible to everyone, it's already funded. | Cheaper code review, multiplayer sessions |
| **Acts, doesn't just show** | At every price point, people pay for tools that *do* something. Sourcegraph sold search; it's Enterprise-only at $16K now. | The dashboard, as such |
| **Fires unprompted** | Anything a user would think to ask for, an agent with shell access already does — for cents, in seconds. | Anything you have to open |

That last test is the sharp one. Orrery's whole function is a *query*: read the
filesystem and git plumbing, derive state. Claude Code can run that query on demand.
**Six ghost worktrees sat for 68 days not because nothing could find them, but
because nobody asked.** The value is in what happens when nobody asks.

---

## Direction 1 · From a window to a notice

**The change:** stop being a thing you open. Become a thing that tells you.

Claude Code ships hooks. A session ends, something fires, and it checks what that
session left behind — across the whole workspace, not just the repo you were in.
No dashboard, no remembering, no asking.

Concretely, unprompted, at the moment it matters:

> *shelf has had an unfinished agent session and 3 uncommitted files for 11 days.
> Your stated focus there was "tighten the resolver cache."*

**Why it passes all four tests:** git-anchored; only the 28-repo workspace vantage
can see it (no agent watches every repo on a timer, no vendor sees outside its own);
it acts; and it fires when you weren't thinking about it — which is exactly the
condition under which the ghost worktrees accumulated.

Everything it needs is already collected. What changes is delivery, not data.

**Related existing surface:** `orrery status --strict` is already a primitive
version — a check that *blocks* rather than displays
(`orrery status --strict && ./deploy.sh`). Extending it with agent-aware conditions
— an unfinished session on this repo, a worktree holding uncommitted work — is the
same move at the other end of the day.

## Direction 2 · The unified per-repo timeline

**This was already identified and never built.**
[`multitool-sessions-plan.md`](multitool-sessions-plan.md) calls it out under
"Bonus the data unlocks": *"a per-repo, cross-tool timeline: everything that touched
one repo, every agent, in one frame."*

One repo, one time axis, every stream Orrery already holds:

- agent sessions (Claude *and* Cursor, tagged by source)
- commits
- branch and worktree events
- what's still uncommitted right now

**Why this is the honest version of "see it all in one place":** every vendor shows
you only its own sessions. Cursor will never show you Claude Code's work. GitHub
shows you what reached a PR. Nothing joins the local streams together, and the
survey evidence says people run **2.4 tools simultaneously** (n=396, Apr–May 2026),
so the fragmentation is real.

### The constraint that keeps it honest

**Git carries no tool attribution and never will.** `multitool-sessions-plan.md`
settled this: only each tool's own session log knows it was Claude or Cursor;
commits record who *you* are. The plan explicitly rejected guessing a commit's tool
from branch/time correlation, because Work Log feeds *Copy as standup* — "a guessed
label would be a lie on the one surface you hand to other people."

So the timeline shows **two truthful streams on one axis. It does not claim
causation.** You see that a Claude session touched these twelve files between 09:00
and 12:30, and that these three commits landed at 12:41. You are not told the second
came from the first, because that can't be known.

That constraint is a feature. It's the same discipline that makes the whole app
trustworthy — it doesn't lie about state.

## How the two combine

They're one product, not two.

**The timeline is the surface. The notice is the delivery.** Something fires
unprompted — a session ended badly, a repo has gone quiet mid-push — and the thing
it opens onto is the per-repo timeline, which shows you the whole story in one
frame rather than making you reconstruct it.

That inverts the current model. Today: open the window, scan for problems. Then:
get told, then look.

---

## What this is, and isn't

**It is a substantially better tool.** Both directions use data already collected,
both are git-anchored, both are things no vendor and no agent will do.

**It is not a business, and shouldn't be built as one.** Everything in
[`WHO-PAYS.md`](WHO-PAYS.md) says single-player local tools don't monetize:
developers pay for the harness and essentially nothing else; every adjacent category
with money has an org as the buyer; Sourcegraph did this exact thing at $2.6B and
retreated to Enterprise-only.

Orrery is free, open source and donation-supported. **Getting materially better at
its stated job is the right target** — not finding a price.

## Sequencing

Neither direction is scheduled; this file says *what*, `ROADMAP.md` says *when*.
Rough order if picked up:

1. **Timeline first.** It's additive, uses collected data, needs no new plumbing,
   and is the surface the notices would point at. Lower risk.
2. **Notices second**, once there's somewhere for them to land. Start with the
   session-end hook — narrowest trigger, clearest moment.
3. **Gate conditions third** — extending `--strict`, which already exists.

## What would change this

- **Anthropic ships workspace-wide session awareness.** Cross-session messaging and
  agent view are currently scoped to *your own* sessions on one machine; if that
  widens to "what's happening across all your repos," Direction 1 is absorbed.
- **The 2.4-tools number falls.** If consolidation means most developers run one
  agent, the cross-tool join in Direction 2 loses most of its point. Worth
  re-checking annually — and note the intersection of what vendors expose is
  already shrinking (see [`STRANDED-WORKTREES.md`](STRANDED-WORKTREES.md) §02).
