# Roadmap

Ordered by priority. Updated at the end of every session — check off completed
items, reorder if priorities shifted, add anything new. Now / Next / Later.

---

## The wedge (read before prioritising)

**Revised 2026-08-21.** [`PRODUCT.md`](../PRODUCT.md) changed direction: Orrery is
**housekeeping that speaks, not observability you visit.** Prioritise against that.

**What survived from the old wedge:** the differentiator is *the state your agents
leave behind across many repos* — Worktrees, Sessions, the token chart. Nobody else
ships it. That's still true and still the ground.

**What changed:** "be the dashboard" was wrong. The maintainer stopped opening the
dashboard. A window loses to an agent that can derive the same state on demand — the
six ghost worktrees sat for 68 days not because nothing could find them, but because
nobody asked.

**And the second lesson from 2026-07-16 was the important one all along:** faced
with a real problem, the maintainer wrote a **bash script**, not a window. The CLI
isn't a side quest — it's the surface. It also routes around Gatekeeper and
notarization entirely, which now demotes a chunk of the distribution work below.

### Three tests for anything new

1. **Does it fire without being opened?** If it only works when you remember to
   look, an agent already does it better.
2. **Does it give a verdict, not a table?** "10 safe to delete" beats a list of 28.
3. **Is it git- or filesystem-anchored?** Vendor session formats churn; git doesn't.

Full reasoning in [`DIRECTION.md`](DIRECTION.md). The evidence that the numbers were
wrong before verdicts is in [`BRANCH-RECONCILIATION.md`](BRANCH-RECONCILIATION.md).

## Now

- [ ] **`orrery collisions` — patch-id triage first.** The smallest thing that
      delivers the new direction, and the only capability the research confirmed
      nobody offers. Three passes, verdict-first:
      1. **Patch-id triage** (`git cherry`) — which branches are *already in main*
         via squash-merge. `git branch --merged` cannot tell you this. In
         `wp-diagnostic` that's **10 of 28**; here it's **8 of 15**.
      2. **Mergeability** (`git merge-tree`) — of what's left, which land clean.
      3. **File collisions** — which branches touch the same files.
      Output leads with the verdict: *"10 safe to delete · 6 land clean · 6 need
      you."* Optional `weave preview` pass when weave is installed (it cleared 25%
      of remaining conflicts). Evidence:
      [`BRANCH-RECONCILIATION.md`](BRANCH-RECONCILIATION.md) §01.

## Next — the direction

- [ ] **SessionEnd hook → the first notice.** A Claude Code session ends; Orrery
      checks what it left across the workspace and says so. No window, no asking.
      Narrowest trigger, clearest moment. This is Direction 1 in
      [`DIRECTION.md`](DIRECTION.md) made concrete.
- [ ] **Verdict-first `orrery status`.** Lead every command with a recommendation,
      not a table. State becomes the detail underneath.
- [ ] **`pre-push` notice** — *"2 in-flight branches already touch
      `scan-email.js`."* Prevention at the moment it's actionable, which is worth
      more than cleanup after.
- [ ] **Per-repo cross-tool timeline** — every stream on one axis (Claude and
      Cursor sessions, commits, branch/worktree events). Already identified as an
      unbuilt bonus in [`multitool-sessions-plan.md`](multitool-sessions-plan.md).
      **Constraint:** git carries no tool attribution, so it shows two truthful
      streams and never claims causation.

## Next — real bugs, unaffected by the direction change

- [ ] **Uncloned repos can't be grouped or annotated**
      ([#40](https://github.com/jokeane9/orrery/issues/40)) — `resolve.overrides()`
      matches by path, so an uncloned repo can never take a manual group. Fix by
      matching on identity, which `discover()` already does. **A real bug, not a
      preference.**
- [ ] **`roots` ignore list** ([#41](https://github.com/jokeane9/orrery/issues/41)) —
      `~/projects/_archive/` scans as live work. One repo today; archives only grow.
- [ ] **Archive a session** — a reversible "retire this from my view" for the Repo
      graveyard. *End* (SIGTERM) stops a running process but the session lingers as
      `finished`. Archive marks it hidden in local state (the `.jsonl` stays on
      disk) with a "show archived" toggle. The honest answer to "can I delete
      this?" — soft, reversible, keeps the read-only-of-your-exhaust ethos.

## Later — window tier (demoted 2026-08-21)

Not wrong, and not abandoned. These polish a surface that is **no longer the front
door**, so they sit behind anything that fires unprompted. Pick them up when the
window is the thing you're actually in.

- [ ] **⌘K palette** ([#42](https://github.com/jokeane9/orrery/issues/42)) —
      shortcuts stop at ⌘9; 28 projects means 19 have no keyboard path.
- [ ] **Editor onboarding** — thesis before tier/group; `tier` → `<select>`; path
      validation/`.git` check. (UX-AUDIT · detail F2–F4)
- [ ] **Provenance made usable** — legend + clickable "guess" → jump to that field.
      (UX-AUDIT · detail F1/F9)
- [ ] **GitHub error consistency** — replace native `alert()` in sync/clone with
      inline/toast. (UX-AUDIT · detail F6/F7)
- [ ] **Design-system tightening** — consolidate badge vocabulary, type-scale
      tokens, shape-encode git state for colorblindness. (UX-AUDIT · global F4/F7/F8)

## Later — distribution (demoted 2026-08-21)

**The CLI routes around Gatekeeper and notarization entirely.** If the terminal is
the primary surface, this work matters less than it did when the window was the
product. Still worth doing eventually; no longer the thing blocking a launch.

- [ ] **Windows code signing** ([#7](https://github.com/jokeane9/orrery/issues/7)) —
      SignPath enrollment → activates the already-wired step. Owner action.
- [ ] **winget listing** ([#8](https://github.com/jokeane9/orrery/issues/8)) —
      blocked on #7.
- [ ] **macOS notarization** ([#9](https://github.com/jokeane9/orrery/issues/9)) —
      Apple Developer Program ($99/yr) + 6 secrets. CI ready.
- [ ] **Post the launch** — Show HN / r/programming / X drafts ready. Worth
      revisiting the angle: the blog-post-shaped asset now is the **squash-merge
      measurement finding**, which is novel, verifiable, and names an unnamed
      problem. See [`BRANCH-RECONCILIATION.md`](BRANCH-RECONCILIATION.md) §01.

## Later — other

- [ ] **Session handoff bundle** (`orrery session share <id>`) — one portable
      file per agent session: footprint, worktree verdict, diff stat, no
      transcript. Every vendor now shares *transcripts* and is fighting secret
      leakage over it; this shares consequences and structurally can't leak.
      **Proposal** — read [`MULTIPLAYER-SPEC.md`](MULTIPLAYER-SPEC.md) first.
      (A team server for sharing sessions is a **decided no** in the same doc.)
      *Honest note: its likeliest real use is future-you, not a teammate.*
- [ ] **P4 — LLM extraction** ([#15](https://github.com/jokeane9/orrery/issues/15)) —
      feed a repo's CLAUDE.md to Claude to distill card fields for repos without a
      structured block. Opt-in, needs an API key + disclosure. **Deferred by decision.**
- [ ] **Tahoe icon polish** — `.icon` (Icon Composer) + `Assets.car` for macOS 26. Cosmetic. (`platform:mac`)

---

## Deliberate noes

Written down so they don't get relitigated every quarter.

- **"What changed since you last looked" / delta view.** Tempting — it sounds like
  the actual job. But a delta needs remembered state, which fights principle #3
  (live from disk, no database) and adds a sync layer that can drift. The
  attention rollup already answers "what needs you" with zero stored state.
  ⚠️ **Revisit note (2026-08-21):** the new notice-driven direction looks like it
  contradicts this. It doesn't, and the distinction is load-bearing. A notice fires
  on an **event** (a session ended, a push is about to happen) and reports *current*
  state at that moment — no memory of what it told you before. A delta view needs a
  stored "last seen" snapshot. **Event-triggered: yes. Remembered diff: still no.**
  If a notice ever needs to suppress repeats, that's the moment this no gets
  re-argued properly — not quietly eroded.

- **Monetization.** Settled 2026-08-21 in [`WHO-PAYS.md`](WHO-PAYS.md) and
  [`PRODUCT.md`](../PRODUCT.md). Dev tools sell a time saving to someone who doesn't
  own the time; tools that *do* the work sell, tools that *help* don't. Orrery
  helps. It stays free, open source and donation-supported. Being better at the job
  is the target, not finding a price.

- **Multiplayer, team servers, compliance/audit positioning.** Each closed with
  evidence — [`MULTIPLAYER-SPEC.md`](MULTIPLAYER-SPEC.md). Vendors shipped shared
  agent sessions inside eight months; every independent attempt died; seven
  regulatory regimes distinguish nothing about AI-written code.

- **Building a merge tool.** [`weave`](https://github.com/Ataraxy-Labs/weave) does
  entity-level merge well and cleared 25% of our conflicts outright. Depend on it,
  don't rebuild it.
- **CI / build status.** Users will ask. PRODUCT.md's non-goal stands: scraping CI
  means tokens, network, and polling in the render path — that's a different
  product, and it breaks the offline-engine principle (#4).

## Completed

- [x] 2026-07-17 — **"Needs attention" cries wolf fixed** (v2.2.1, #44):
      `collect()` counted every unmerged *remote* branch, so repos cloned to
      read flagged on hundreds of upstream PRs (langflow: 1884). Now counts
      local branches only — 19→14 projects flagged, 2374→12 unmerged, all real.
      `collect()` had no test; now it does.
- [x] 2026-07-16 — **CLI + Sessions** (v2.2.0, #45/#46): the wedge, made
      deliberate. **Sessions** — every Claude Code session per repo (live/idle,
      branch, span, msgs, tokens) and the join that matters: a session whose
      worktree is still on disk is flagged *left a worktree*. Metadata only,
      never content (pinned by a test that plants a secret). Falls out of the
      *same* transcript pass the Work Log already did, so warm render is
      unchanged. **CLI** — `orrery status/worktrees/sessions/standup/skills`,
      `--json`, `--strict` as a deploy gate; reads the installed app's config so
      both surfaces agree. Forced `generate.workspace()` out of the HTML render,
      so the GUI and CLI can't disagree about what needs you.
      Shipped as ONE release: #46 was stacked on #45 and squash-merged first, so
      both landed in one commit — merging #45 afterwards would have *deleted*
      Sessions (663 deletions). Lesson: merge the base of a stack first.
      Learned along the way: transcripts are pruned at ~29 days, so the
      Sessions↔Worktrees join has a horizon and could never explain the 68-day
      ghost that started all this. Worktrees persist; sessions expire.
- [x] 2026-07-16 — **v2.0.0 — renamed Mission Control → Orrery** (#37): the old
      name collided with Apple's window manager, and not cosmetically —
      `open -a "Mission Control"` silently launched Apple's app, so the most
      common scripted launch path did nothing. Carried three migrations, each of
      which fails silently if it regresses: data dir (config would be orphaned →
      app opens empty), keychain service (token orphaned → looks like a logout),
      and per-repo `.mission-control.*` block files (live in *users'* repos, so
      the fallback is permanent). Cask renamed with `cask_renames.json`; verified
      a real 1.7.0 → 2.0.0 upgrade preserving config byte-for-byte.
- [x] 2026-07-16 — **Worktrees view** (v1.7.0, #36): `views.collect_worktrees()`
      + a workspace tab listing every extra checkout — repo, path, branch/
      detached, age, uncommitted, unmerged — each with a safe-to-remove verdict
      (clean tree AND HEAD reachable from a branch; anything else says NO and
      why). Closes the invisible-state hole: ghost worktrees left under
      `.claude/worktrees/` by interrupted Claude Code sessions, which no
      `git status` reports. Ported from a local bash script, fixing its
      macOS-only `stat -f %m` (would have broken the Windows build) and its
      dead unmerged count.
- [x] 2026-07-14 — **Groups become folders + triage + keyboard a11y** (v1.6.0,
      #33): click-a-group folder filter + breadcrumb, drag-and-drop reorder/move
      (localStorage), attention rollup dots, attention→tier sort, WCAG-AA
      contrast + keyboard operability. Built from the 5-agent UX audit
      ([`UX-AUDIT.md`](UX-AUDIT.md), [`UX-FLOWS.md`](UX-FLOWS.md)).
- [x] 2026-07-14 — **Auto-organized project groups** (v1.5.0, #32):
      `resolve.auto_groups()` (name-prefix → owner → parent-dir) + collapsible
      sidebar groups + manual `Group` editor override.
- [x] 2026-07-14 — **macOS Open-Anyway cask caveats** (#31 + live tap): brew
      prints the first-launch Gatekeeper steps. Real fix is notarization (#9).
- [x] 2026-07-14 — **Regen errors are logged, not swallowed** (v1.4.1, #30):
      `app.py._log_exc` → DATA/error.log. (After a QA false-alarm where a stale
      instance masqueraded as a broken build — see `_log.md`.)
- [x] 2026-07-14 — **PM scratchpad tab + canonical `PRODUCT.md`** (v1.4.0,
      #28): a local autosaving admin notes view (bridge-gated like the config
      editor; `pm_notes.md` in the data dir, gitignored) and the first product
      doc. Sync/login captured as a deliberate no in PRODUCT.md's open
      questions, not built.
- [x] 2026-07-14 — **Top-level views epic** (v1.3.0): Skills catalog (#24),
      Work Log — commits chart + list + standup copy + overview Today line
      (#25), Roadmap aggregator (#26), per-day Claude token chart with a
      transcript cache (#27). All render-path only; `views.py` new stdlib
      sibling module.

- [x] 2026-07-12 — Auto-populate epic (#15), P1→P3.2 merged: local discovery +
      resolver (#16), provenance badge (#17), P2 auto-maps (#18), P3.1 GitHub
      auth — keychain token (#19), P3.2 GitHub sync — repos→cache→cards incl.
      uncloned (#20). Local scan offline; GitHub opt-in; token/network stay out
      of the render path. (P4 LLM extraction deferred.)
- [x] 2026-07-12 — Merge sweep: cleared 5 stale Dependabot PRs (#2–#6) +
      P3.2 (#20); main clean, 0 open PRs
- [x] 2026-07-12 — In-app config editor (#13), shipped in v1.1.0 — add/edit/
      delete projects from a form; verified end-to-end in the real app
- [x] 2026-07-12 — PM + CI/CD scaffolding: CLAUDE.md, project-management/ docs,
      guardrail `ci.yml` (lint + render smoke + both-platform build on PRs),
      branch protection on `main` (requires CI), CHANGELOG, Dependabot,
      issue/PR templates, labels + v1.1 milestone, roadmap seeded to issues #7–#13
- [x] 2026-07-12 — Cross-platform refactor (per-user data dir when frozen,
      first-run sample seeding, Ctrl labels on Windows, configurable viz tools)
- [x] 2026-07-12 — Packaging: PyInstaller spec, mac sign/notarize/staple script,
      Windows Inno Setup installer w/ WebView2 bootstrap, icon.ico generator
- [x] 2026-07-12 — CI release workflow: v* tag → build both → publish → bump tap
- [x] 2026-07-12 — Public repo + Homebrew tap set up; v1.0.0–v1.0.2 released;
      auto-bump proven end-to-end
- [x] 2026-07-12 — Docs: CLAUDE.md, DISTRIBUTION.md, project-management/, README
