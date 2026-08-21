# Multiplayer — decision record, brief and spec

**The canonical file on anything team / sharing / multi-user shaped.** Prompted by
Aaron Epstein's "Multiplayer AI" call. Four commissioned probes, seven reports,
every load-bearing claim re-verified by hand against primary sources or the
GitHub API.

*2026-08-20 · extends [`TEAM-COLLAB-RESEARCH.md`](TEAM-COLLAB-RESEARCH.md).*

---

## PM summary

We asked whether Orrery should become multiplayer — shared agent sessions, a team
server, sessions passed between developers.

**The answer is no.** Not because the idea is bad, but because it's already taken.
While we were deciding, five vendors shipped it: Zed Delta landed eight days
before this brief, Warp and Amp are live, Cursor has had it since December. The
independent attempts all died — roughly thirty projects, two with any traction,
and the one that did *exactly* what we specced (sessions passed via git) got 15
stars and 1 fork before being abandoned. The strongest demand signal anyone found
in eighteen months is a GitHub issue with six thumbs-up.

Three adjacent ideas were tested on the way and also failed: **agent-to-agent
handoff** has no market and no accepted standard; **compliance positioning** has
no legal hook at all across seven regimes; **manager-facing rollups** hit the same
surveillance wall we already documented in August.

One thing survives, on narrow but real ground. Every vendor shares *transcripts*,
and transcripts leak secrets — Amp pulled public sharing over exactly this, and
Cursor admits its redaction can miss things. **A bundle that carries consequences
instead of conversation — footprint, git state, stranded worktrees, no transcript
— structurally cannot leak.** That's a week of work and it doesn't touch the
local-first promise.

The pattern underneath all of it is the useful part: **everything session-anchored
died; everything git-anchored or single-player is working.** Sessions belong to
vendors and their formats churn. Git doesn't.

## Recommendations

**Do**

1. **Ship the handoff bundle** if you want it — `orrery session share <id>`, three
   phases, one MINOR release, about a week. Optional, not urgent. Honest framing:
   its likeliest real use is future-you, not a teammate.
2. **Keep the per-tool source tag** in Sessions. It's under mild challenge (§06)
   but the challenge doesn't apply to a private dashboard.
3. **Fix the $420M figure** in `TEAM-COLLAB-RESEARCH.md` — it's flagged 🟢 Strong
   and can't be traced to a real source (§07).
4. **Look at the worktree orchestrators** — Vibe Kanban, Conductor, Claude Squad,
   Superset, Paneflow. They're a real competitive set we've never named, and
   they're converging on the position this research points at.

**Don't**

5. **Don't build a team server, a wire, or live co-presence.** Decided; see §02.
   Don't reopen without the checks in §09.
6. **Don't position anything as compliance.** There is no obligation, and saying
   otherwise repeats a false legal claim to buyers who can check (§05).

**Watch**

7. **Stay git-anchored.** The durable edge isn't sessions, isn't cross-vendor,
   isn't multiplayer — it's that git and the filesystem don't churn and vendor
   session formats do.

---

## 01 · The verdict board

Parallel decisions, not a sequence.

| | Decision | Why |
|---|---|---|
| **BUILD** | Session handoff bundle — `orrery session share <id>` | Everyone shares transcripts and loses to secret leakage. A bundle with no transcript can't leak. ~1 week, principle #1 untouched. |
| **KEEP** | Per-tool source tag in Sessions | Challenged by the kernel's reversal, but that's about public commit trailers, not a private dashboard. |
| **NO** | A team server for sharing sessions | Vendors shipped it, startups are racing it, nobody's asking. |
| **NO** | Git as the wire (transport B) | `claude-git-sessions` is literally this: **15★ / 1 fork**, abandoned 2026-06. |
| **NO** | Live co-presence and takeover | Vendor territory; Anthropic blocks it by design. |
| **NO** | Compliance / audit-trail positioning | Seven regimes, unanimous no. NIST declined in writing. |
| **NO** | Agent-to-agent handoff as the primary bet | No market, no standard. Cheap hedge only — `--json` already serves it. |
| **NO** | Any manager-facing rollup | The Aug-10 surveillance wall, third time from a new direction. |

---

## 02 · Why the team server is dead

**1 · The vendors already shipped it.** Not "might" — did, mostly in eight months.

| Vendor | What shipped | When |
|---|---|---|
| **Zed Delta** | Multiplayer agent threads — join, comment, *"continue a task later"*; connects to Claude Code | 2026-08-12, private beta |
| **Warp** | Live shared sessions; viewers with edit access send queries and run commands; wraps Claude Code, Codex, OpenCode | shipped |
| **Amp** | Multiplayer orbs — join thread, message agent, shared terminal | 2026-07-22 |
| **Cursor** | Team-visible agents + admin-gated team follow-ups; shared transcripts with "Fork to Cursor" | 2025-12-18 onward |
| **Anthropic** | Team-visible web sessions (static); `--teleport` requires the same account | — |
| **GitHub** | Repo-scoped agent visibility; explicitly no steering | 2026-01-26 |

Read-only sharing is table stakes at five of eight. Live takeover shipped at three
inside eight months, and three YC startups (Mosaic S26, Skillsync W26,
mobsession.ai) are racing the rest.

**2 · Every independent attempt died.** Verified against the GitHub API:

| Repo | What it is | ★ / forks |
|---|---|---|
| `ingram-technologies/claude-git-sessions` | **Sessions passed via git — literally transport B** | 15 / 1, abandoned 2026-06 |
| `z2z23n0/agent-capsule` | Export → receiver imports and continues | 8 / 2 |
| `EliranG/claude-duet` | Two devs, one session, WebRTC | 142 / 8, dead in 11 days |
| `chadbyte/clay` | Self-hosted team workspace | 385 / 53 — the only survivor |
| — *compare* — | | |
| `matt1398/claude-devtools` | **Read your own transcripts** | 3,850 / 293 |

~30 projects, two with traction. People want to read their own sessions, not each
other's.

**3 · The demand artifact doesn't exist.** Strongest verified signal in eighteen
months: a Claude Code issue at **+6**. Zed's Delta launch hit 679 points on HN
with roughly 80% skeptical comments (*"coding is a single-player game"*); the
sympathetic minority argued for **async handoff**, not live pairing.

Two traps, both hit on earlier passes: CC issues #15881 (+60) and #11455 (+25)
look like demand and are **same-person** continuity requests. Amp's "handoff"
command is also same-person. Check the person boundary every time.

### The wall, for the record

Multiplayer means shared state; principle #1 says no server, no accounts. Three
transports were considered:

- **A — a file the user sends.** Costs the principle nothing: exporting is the
  user's action, not the app's. **This is the bundle.**
- **B — git as the wire.** Was the recommended follow-up in the first draft.
  Killed by the 15★/1-fork datapoint above.
- **C — peer/LAN or a relay.** Inverts principle #1; would need a `PRODUCT.md`
  pivot note first. Not without that, and the research says not at all.

---

## 03 · What survives, and why it got stronger

**Amp killed public thread sharing on 2026-06-02** — *"It's getting too hard to
review a thread to ensure it doesn't contain any snippets of sensitive files."*
Cursor's docs warn its redaction can miss secrets. Cursor also shipped cross-user
session access *accidentally* and treated it as a security defect.

Everyone in this lane shares **transcripts**, and transcripts leak secrets. It is
the load-bearing design problem of the entire category.

**Our bundle has no transcript.** Paths, branch names, counts, a worktree verdict —
nothing anyone typed. It cannot leak the thing that leaks, because it does not
contain it. That is not a feature to add; it is already the Sessions view's rule,
enforced by `test_footprint_never_leaks_*`.

**Everyone else shares the conversation. We share the consequences.** A Cursor
share link will never tell you three uncommitted files are stranded in
`.claude/worktrees/agent-abc8ed` — that isn't in their data model; it's on your
disk.

---

## 04 · Who the recipient actually is

Not a reviewer reading a diff, and not the next agent.

- **Agent-to-agent is not a market.** The MCP "Agent Handoff Protocol" (SEP #2683)
  is open, unsponsored, unmerged. Nobody sells the payload.
- **Humans didn't leave review — their input device changed.** Of human comments
  on AI-authored PRs, **65.53%** are direct review and **25.92% are agent-steering
  commands**; on human-authored PRs 93.56% are review. (33,596 PRs,
  arXiv 2605.02273, verified.)
- **Bot-only review underperforms**: 45.20% merge rate vs 68.37% human-reviewed
  (3,109 PRs, arXiv 2604.03196).
- **Review is the bottleneck, not a shrinking target**: median time in review
  **+441.5%**, time to first review +156.6% (Faros, 22,000 devs, verified).

**Build for the human about to type the next instruction.** They need "what did it
touch, where did it stop, what did it leave stranded" fast enough to write a good
prompt — not fast enough to read 241 lines.

---

## 05 · Compliance is closed

An earlier draft claimed *"EU AI Act Article 14 became enforceable 2026-08-02"*
and proposed selling the session record as an audit artifact. **That was false on
the date and on the substance.**

- **The date moved.** Regulation (EU) 2026/1744 (Digital Omnibus on AI) entered
  into force 2026-07-27 — six days before the old deadline — deferring high-risk
  Arts 8–17 + Annex III to **2027-12-02**. Verified against the
  [Commission's own timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act).
  What applied on 2026-08-02 was Art 50 transparency plus enforcement powers.
- **Article 14 has no logging duty.** It's a *design capability* requirement. None
  of its five paragraphs require recording anything. Art 12 covers the deployed
  system's **runtime** logs, not its development.
- **It binds high-risk systems only, and coding tools aren't one.** Annex III is a
  closed list of eight categories; software development appears nowhere. Orrery
  isn't even an AI system under Recital 12 — it's a deterministic reader of git.
- **The Commission excluded source code** from the Art 50 marking obligation.

**And it isn't just the AI Act.** Seven regimes checked — **EU Cyber Resilience
Act, IEC 62304, FDA, SOC 2, PCI-DSS, SOX/PCAOB, DORA** — unanimously no. None
distinguishes AI-generated from human-written code. What they require is
*segregation of duties* — reviewer ≠ author — which git and PR review already
produce, and which is about **people, not models**.

The decisive citation, verified verbatim from
[NIST SP 800-218A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf):

> "Practices and tasks in this Profile do not distinguish between human-written
> and AI-generated source code, because it is assumed that all source code should
> be evaluated for vulnerabilities and other issues before use."

That is the standards body considering this exact question and declining.

**No BOM format has a field for it either** — CycloneDX `authors` is
component-level, SPDX 3.0's AI Profile describes AI *packages*, CISA's 2026 SBOM
Minimum Elements adds no elements for AI systems. SLSA is build provenance and its
threat model lists forged attribution as explicitly *not addressed*.

**Nobody credible sells this.** The vendors pushing an AI-Act line cite the
superseded date and invent Article 12 requirements; one concedes mid-page that
AI-generated code doesn't trigger high-risk obligations. **CodeSlick shipped this
exact thesis and shut down in June 2026** — *"the paying customers weren't
there."*

---

## 06 · What the compliance probe found instead — archaeology

- **`git-ai-project/git-ai` — 2,477★ / 275 forks**, active, on the Thoughtworks
  Radar (Assess). A git extension tracking AI-generated code. Its pitch is
  **accountability and code understanding**, not compliance. (Verified via API.)
- **The articulated user need**, verbatim: *"an AI agent would make changes to our
  codebase, and a week later nobody could explain why."*
- **Cursor's Agent Trace spec** has ten partners (Amp, Cline, Cloudflare,
  Cognition, Jules, Vercel…). Motivation is understanding AI vs human work —
  compliance conspicuously absent. Adoption currently thin.

### The norm layer is contradictory — don't build on it

- **The kernel tried model identity and deleted it.** The original policy
  (Dec 2025) required `Assisted-by: AGENT_NAME:MODEL_VERSION`. Commit
  [`816d9992d9`](https://github.com/torvalds/linux/commit/816d9992d9)
  (2026-07-01) removed it: *"The requirement to identify specific models… provides
  free advertising to proprietary software companies while adding little or no
  useful information."* Current tree reads `Assisted-by: LLM [TOOL1] [TOOL2]` —
  **verified against `Documentation/process/coding-assistants.rst` on master**,
  not the docs site, which still serves the stale format.
- **Kubernetes prohibits the tag outright** (2026-06-26) — no AI co-author, no
  `assisted-by` or `co-developed` trailers — requiring prose disclosure instead.
- **Debian's GR** (voted 2026-08-15 → 08-28) had eight competing proposals and
  **not one asked for model identity.** Fedora, ASF, curl, CPython: same. *Whether*,
  never *which*.

**This lands on a decision we already shipped.** The Sessions view tags each row by
tool, and the kernel's judgment is that tool identity adds *"little or no useful
information."* Two reasons not to panic: their objection is to **public commit
trailers as vendor advertising**, which a private local dashboard isn't; and
`multitool-sessions-plan.md` justified the tag on different grounds — only the
tool's own log knows which tool ran, and you need it to know where to go back to.
Counter-signal: kernel contributors **voluntarily** write `Assisted-by: Claude…`
(~830 commits, approx.) far more than the mandated generic form (~40). The pull is
bottom-up developer behaviour, not top-down requirement.

**The tension to hold:** the same record is a *trust tool* when the author or a
maintainer reads it, and a *surveillance tool* when a manager does. Microsoft
flipped `git.addAICoAuthor` on in VS Code and had to revert it — 241👎 vs 29👍 —
while a proposal to record the same fact under a different word got 72👍 / 0👎.
The objection is to being advertised and measured, not to the record existing.

---

## 07 · The spec — `orrery session share <id>`

```sh
orrery session share <id>              # → orrery-session-<id>.html
orrery session share <id> --json       # raw payload, for piping
orrery session share <id> -o PATH
```

GUI: a **Share** control on the session row, beside the existing **End** control.
Second verb on a session, not a new view.

### Payload

| Field | Source |
|---|---|
| `id`, `source`, `title`, `repo`, `branch(es)` | session dict |
| `lifecycle` | `_lifecycle()`, stamped with export time |
| `footprint` | files, dirs, tools, PRs — **paths and names only** |
| `worktree` | path, dirty, unmerged, existing safe-to-remove verdict |
| `diff_stat` | `git diff --stat` — **stat only, never patch text** |
| `resume` | the command to continue it, with preconditions stated |
| `exported_by`, `exported_at` | so a stale bundle is obvious |

One self-contained file; needs neither Orrery nor Python on the receiving end.
Reuse the existing stylesheet and session-row markup.

### Privacy rule (non-negotiable — and the whole differentiator)

**Metadata only. No prompt text, no response text, no patch bodies, ever.** Extend
`test_footprint_never_leaks_*` to the share path with a planted secret in a
transcript *and* in a working-tree diff.

### Phases

1. `views.session_bundle()` → dict. Pure function, tests + leak guard. Shippable
   alone behind `--json`.
2. Renderer → self-contained HTML. `orrery session share` lands here.
3. Share control in the GUI.

One MINOR release.

### Risks

- **Table stakes moved.** Read-only session sharing is free at four vendors. The
  bundle must lead with what they don't carry — worktrees and git consequences —
  or it reads as a worse version of a feature people already have.
- **The `resume` line is a lie waiting to happen.** Different checkout, branch or
  tool version and it's wrong. Anthropic blocks cross-account resume outright, so
  a bundle can suggest, never promise. Transcripts also prune at ~29 days, so a
  bundle pointing at a vanished session must fail readably.
- **This may just be single-player.** The likeliest real use is exporting for
  *future you*. Still useful, but smaller than "multiplayer" implies — and the
  3,850★ read-your-own-transcripts tool suggests that's where the pull is.

---

## 08 · Deliberately not building

- **A team server, hosted or self-hosted.**
- **Live co-presence / takeover.** Vendors own it; Anthropic blocks it by design.
- **Transport B (git as the wire).** `claude-git-sessions` is exactly this and got
  15 stars and 1 fork.
- **Anywhere bundles are collected centrally.** The Aug-10 no, in a hat.
- **Manager-facing rollups.** Same reason as Aug-10.
- **Compliance positioning.** No obligation exists; saying otherwise is a false
  claim to buyers who can check.

---

## 09 · What would reopen this

Any two → transport B gets a real decision. All three → transport C is worth a
`PRODUCT.md` pivot note.

1. **Bundles get sent** — ours, then someone else's, unprompted.
2. **Somebody asks for the wire** — developers, not managers. (Aug-10 check #3.)
3. **A well-adopted cross-person handoff tool appears** — hundreds of forks, not
   tens of stars, and not a cost dashboard. Best comparable today has 3 forks.

---

## 10 · Corrections to other docs

- **`TEAM-COLLAB-RESEARCH.md`: the $420M AI-code-review ARR figure is
  unverified** — traceable only to SEO content farms citing each other. Flagged
  🟢 Strong; should be downgraded. CodeRabbit's $40M ARR and $1.5B Series B are
  better attested but still secondary.
- **We have an unnamed competitive set**: worktree orchestrators — Vibe Kanban,
  Conductor, Claude Squad, Superset, Paneflow. By April 2026 nearly every major AI
  coding tool shipped worktree support. They surface handoff summaries *to
  humans* — the exact position this research points at. Needs a real look.
- **Ignore `Leanmcp/superview.sh`** (2,112★ / 2,128 forks) if cited anywhere —
  forks exceeding stars with unrelated fork names is a star-farm artifact.

### Corrections made mid-run to this doc's own claims

| Was | Now |
|---|---|
| EU AI Act Art 14 enforceable 2026-08-02, creating an audit-trail obligation | False on date *and* substance — see §05 |
| The bundle's real recipient is the next agent | No market; the recipient is the human steering the agent — §04 |
| The kernel's `Assisted-by:` shows a converging norm | No convergence — Kubernetes prohibits it, the kernel deleted model identity, Debian's eight proposals ask none — §06 |

---

## 11 · Bottom line

Every idea that died was **session-anchored** — team server, git-as-transport,
agent-to-agent, live takeover. Every idea that's working is **git-anchored or
single-player** — reading your own transcripts at 3,850★, tracking AI code in git
at 2,477★, and the Worktrees view already shipped.

That isn't a coincidence. Sessions belong to vendors and their formats churn —
Claude Code's JSONL is documented as unstable/internal and Cursor's schema has no
contract. Git and the filesystem don't churn. In eighteen months worktrees will
still strand, and no `git status` will still not mention them.

**Multiplayer is interesting, and the instinct that it was early was half right.
It isn't early — it's occupied.**

---

*Research gaps: Reddit unreachable behind bot checks; the CSA control workbook,
the SIG 2026 questionnaire and ISO/IEC 42001 Annex A are registration- or
paywall-gated; Warp's sharing tier, whether an Amp teammate can continue someone
else's thread, and Mosaic/Skillsync's shipped depth are unverified.*
