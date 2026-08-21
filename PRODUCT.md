# Orrery — Product

The canonical product doc. What this is, who it's for, what it deliberately is
*not*, and how we'll know it's working. Engineering/process lives in
[`project-management/`](project-management/); this file is the *product* north
star. If a product decision isn't captured here, it's not decided.

> **Revised 2026-08-21 — deliberate change of direction.** Orrery was defined as a
> dashboard whose north star was *"the first window you open and the one you keep
> open."* Its own maintainer stopped opening it. That is a product failure, not a
> marketing one, and §*Why this changed* records the evidence. The direction is now
> **housekeeping that speaks, not observability you visit.**

---

## One-liner

**Orrery tells you what your agents left behind across every repo — you don't ask
it, and you don't open it.**

The insight underneath it: agentic coding abstracts *doing* into *directing*, so
the ground-truth model you used to build for free — every branch, edit, and stray
checkout that passed through your hands — is gone. Worse, an agent will happily
regenerate that state on demand *if you think to ask*, and the whole nature of this
mess is that you don't know there's anything to ask about. Six stranded worktrees
sat for 68 days; 28 branches accumulated in 17 days; ten of them were already
merged and could have been deleted at any time.

**Orrery's job is to notice, and to say something.**

## What it is

A local tool that reads your git repos and your agents' own logs, and **surfaces
what needs you** — unprompted, at the moment it's actionable.

Three surfaces, in order of importance:

1. **Notices.** Fired from hooks (a Claude Code session ending, a `pre-push`) or a
   timer. This is the product. *"shelf has had an unfinished agent session and 3
   uncommitted files for 11 days."*
2. **The CLI.** `orrery status`, `orrery sessions`, `orrery worktrees`,
   `orrery collisions`, all with `--json`. Where you act on what you were told.
3. **The window.** A detail view you land in when a notice points at something —
   project cards, Sessions, Work Log, Skills, Roadmap, Worktrees, PM scratchpad.
   Still good. No longer the front door.

Everything is read live from disk; the human facts live in one editable JSON file.
Nothing leaves the machine.

## The verdict, not the state

The single most important distinction in this document.

**Observability** says: *here is the state of 28 repos, you figure it out.* That is
what Orrery did, and it is why its own author stopped opening it.

**Housekeeping** says: *10 of these branches are safe to delete right now, 6 have
work that lands clean, 6 need you.*

That second output took three cheap checks — patch-id triage, a virtual merge, an
entity-level merge preview — and **nothing else in the ecosystem produces it.**
`git branch --merged` lies under squash-merge, GitHub can't see local state, and
every agent orchestrator scans only its own directory.

**Lead with the verdict. The table of state is secondary.** See
[`BRANCH-RECONCILIATION.md`](project-management/BRANCH-RECONCILIATION.md) §01.

## Who it's for

The developer running many repos with agents — side projects, client work, a
monorepo split into pieces — who has more parallel work in flight than they can
hold in their head, and no longer knows what the agents left behind.

**This is not a team problem and doesn't need to be.** One person running parallel
agents generates what a team used to generate: 28 unmerged branches in 17 days,
solo, with seven branches editing the same file. Built for that person first.

## Principles (the non-negotiables)

1. **Local-first, no accounts, no telemetry, no server.** Nothing leaves the
   machine. A product promise, not just an architecture note — features that
   require a backend or an account are out of scope by default.
2. **One app, two platforms, one version.** A single codebase builds the macOS and
   Windows apps from the same commit and version number. Never fork the platforms.
3. **Live from disk, not a database.** Git state is always the real current state.
   No sync layer to drift.
4. **The engine stays stdlib-only and offline.** `generate.py` + `resolve.py` have
   no dependencies and never touch the network. Anything networked (GitHub) is an
   opt-in, isolated module reading a cache file.
5. **Human facts are cheap to edit and they survive.** One JSON file, an in-app
   editor, provenance badges on auto-derived fields.
6. **It matches its own aesthetic.** GitHub-dark, SF Mono, thin muted marks. Calm,
   dense, not a toy.
7. **It never lies about state.** Where a fact can't be known — git carries no tool
   attribution, Cursor exposes no token counts — Orrery shows honest absence rather
   than a guess. A guessed label on a surface you hand to other people is a lie.
8. **It says something without being opened.** New. If a feature only works when
   you remember to look at it, an agent with shell access already does it better.

## What it is NOT (non-goals)

- **Not a team/cloud product.** No shared state, no multi-user, no cross-device
  sync. Settled twice with evidence — see
  [`TEAM-COLLAB-RESEARCH.md`](project-management/TEAM-COLLAB-RESEARCH.md) and
  [`MULTIPLAYER-SPEC.md`](project-management/MULTIPLAYER-SPEC.md).
- **Not multiplayer.** Zed, Warp, Amp and Cursor all shipped shared agent sessions
  inside eight months; every independent attempt died. Closed.
- **Not a compliance or audit product.** Seven regimes checked; none distinguishes
  AI-written from human-written code, and NIST declined the question in writing.
  Closed.
- **Not a git client.** It surfaces state and verdicts; it doesn't stage, commit,
  rebase, or resolve conflicts. Deleting a branch it has *proven* is already merged
  is the boundary case — explicit, reversible, and opt-in.
- **Not a merge tool.** [`weave`](https://github.com/Ataraxy-Labs/weave) does
  entity-level merge well; it cleared 25% of our conflicts outright. Depend on it,
  don't rebuild it.
- **Not a CI/observability dashboard.** No build logs, no uptime, no metrics.
- **Not a full project-management tool.** The PM tab is a personal scratchpad.
- **Not a business.** See below.

## Success — how we'll know it's working

North star: **the notice arrives before you noticed the problem.** The measure is
whether Orrery tells you something true and actionable that you did not already
know and would not have thought to ask.

Leading signals (a free, local, no-telemetry app — observed, not instrumented):

- **You act on notices.** The branch gets deleted, the session gets ended, the
  worktree gets cleared, because it told you.
- **The maintainer uses it.** The plainest test there is, and the one it currently
  fails.
- **Verdicts, not tables.** New surfaces ship with a recommendation attached.
- **Distribution is frictionless.** `brew install`, no fight on first launch.
- **Organic pickup** among developers running many repos with agents.

Retired signal: *"install → keep, stays in the Dock."* Presence in the Dock was
never the point; it measured a window nobody opens.

## Settled questions

### Is it a business? No.

**Settled 2026-08-21.** Every path was tested and written up in
[`WHO-PAYS.md`](project-management/WHO-PAYS.md). The short version:

- Developers pay for the harness — Cursor ~$2B, Claude Code >$2.5B — and
  essentially nothing else.
- Every adjacent category with real money has an **org** as the buyer, and prices
  per developer *measured*, with viewers free.
- Sourcegraph — the closest analog, a visibility layer over many repos — was worth
  $2.6B in 2021, hasn't raised in five years, killed self-serve, and retreated to
  Enterprise-only at $16K minimum.
- Vibe Kanban shut down with **27,868 stars** because free users don't convert.
- The structural reason: **dev tools sell a time saving to someone who doesn't own
  the time.** Tools that *do* the work sell; tools that *help you* do the work
  don't. Orrery helps.

Orrery stays free, open source, donation-supported. **Being materially better at
its job is the target — not finding a price.** Revisiting this means rewriting this
section first, deliberately.

### Does it sync across devices? Does it need a login?

**No, and that's deliberate.** Real sync means a backend + accounts + data leaving
the machine — a direct trade against principle #1. **Sync isn't a missing feature,
it's a different product.** Standalone, per-machine, no login.

### What's the name?

**Decided: Orrery** (v2.0.0). A desk instrument showing every planet's position at
once, in one frame. It replaced "Mission Control", which collided with Apple's
window manager — and not only cosmetically: `open -a "Mission Control"` resolved to
Apple's app, so the most common scripted launch path silently did nothing.

## Why this changed

Recorded so the reasoning survives the decision.

1. **The maintainer stopped opening it.** Stated plainly, 2026-08-21: *"I don't
   really look at git that much or even Orrery — it's more like, what the fuck is
   going on info."* The north star was "the first window you open." It wasn't.
2. **A window loses to an agent.** Everything Orrery knows is a *query* over the
   filesystem and git — an agent with shell access derives it on demand for cents.
   There is no data moat. The six ghost worktrees sat for 68 days not because
   nothing could find them, but because nobody asked. **The value is in what
   happens when nobody asks.**
3. **The winners in this market fire unprompted.** CodeRabbit never waits to be
   invoked — it reviews every PR automatically, and it's worth $1.5B. Sourcegraph
   sold search, a thing you invoke, and retreated to enterprise-only.
4. **Verdicts beat state, and we proved it locally.** "28 unmerged branches" was
   overcounted by a third; three checks turned it into "10 delete, 6 land, 6 need
   you." The state view had been showing the wrong number the whole time.
5. **Git-anchored survives; session-anchored dies.** Every idea that failed this
   week was anchored to vendor session formats, which churn. Git and the filesystem
   don't churn.

Full reasoning: [`DIRECTION.md`](project-management/DIRECTION.md).

## Where the rest of the truth lives

- [`CLAUDE.md`](CLAUDE.md) — orientation, how it's built, build/run/release.
- [`project-management/README.md`](project-management/README.md) — which PM doc to
  open when.
- [`DIRECTION.md`](project-management/DIRECTION.md) — the four-test filter and the
  candidate directions.
- [`WHO-PAYS.md`](project-management/WHO-PAYS.md) — where money is, and isn't.
- [`DISTRIBUTION.md`](DISTRIBUTION.md) — signing, notarization, the $0 launch path.
