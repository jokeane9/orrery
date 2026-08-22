# Should Orrery become a team product?

**Decision record — team-scale agent collaboration.** Two gated research probes,
August 2026. Answer: **no.** This file exists so the question doesn't get
re-opened from scratch in six months.

*Prepared 2026-08-10 · two Sonnet-5 research probes, adversarial read, key claims
verified by hand · sources at end.*

---

## The decision

**Don't build a team version of Orrery.** Not because the pain is imaginary —
it's real — but because the demand for it is thin, the agent vendors already
give away a version of it inside subscriptions teams pay for anyway, and the one
genuine gap left requires building something that contradicts Orrery's
local-first promise.

Orrery stays single-player. The July 2026 positioning — solo, cross-tool, local,
angled at trust and verification — survives both probes intact and is
re-confirmed by them.

## Key takeaways

| Signal | Takeaway |
|---|---|
| 🔴 **Decisive** | **Someone already built it and nobody came.** `m-shirt/claude-code-tracker` is a self-hosted multi-user Claude Code dashboard — syncs every teammate's `~/.claude/` to a central server, role-based access. **28 stars, 3 forks.** Solo tools in the same space get thousands. The experiment has been run. |
| 🟠 **Caution** | **The vendors are already in this lane, for free.** Anthropic ships Claude Code Team/Enterprise analytics; Cursor ships team usage analytics; GitHub ships Copilot metrics plus Agent HQ. All bundled into subscriptions the target team already buys. |
| 🟠 **Caution** | **The commercial middle is taken too.** Jellyfish sells a Claude Code dashboard with an explicit per-developer "Autonomous Agent Activity" metric; minware, Torii, Portkey, Mavvrik and others sell per-engineer agent spend attribution. |
| 🟡 **Mixed** | **The review/trust bottleneck is where money actually moves** — CodeRabbit ($143M Series C at $1.5B, Aug 2026), Greptile, Graphite-acquired-by-Cursor. Same conclusion as the July scan, reached independently. ⚠️ **Corrected 2026-08-21:** this row originally read 🟢 Strong and sized the category at *"around $420M ARR."* **That figure is fabricated** — traced to a single uncited blog post, and it fails a sanity check by 4–8× against the summed ARR of its own named leaders. The individual company figures stand; the category size does not. See [`WHO-PAYS.md`](WHO-PAYS.md) §02. |
| 🟢 **Strong** | **Agent spend is becoming a real budget line with a named owner.** FinOps Foundation 2026: 98% of practitioners now manage AI spend, up from 31% two years earlier (n=1,192). A buyer that didn't exist — but shopping for cost governance, not activity visibility. |
| 🔵 **Insight** | **The one remaining gap is a surveillance product.** Everything cross-person stops at cost and counts; nobody reads *multiple developers' transcripts* for behaviour. That gap may be empty because it's unpleasant, not because it's unclaimed. |
| 🔴 **Correction** | **"Nearly alone in the local lane" is dead.** Several tools now read the same Claude Code JSONL. Orrery is still differentiated; the claim is not. See §04. |

---

## 01 · How this was tested

Two probes, the second gated on the first.

**Probe 1 — is the pain felt, and does anyone pay?** Came back negative on both.
No team-scale complaints found, no purchase evidence for cross-developer agent
visibility.

**That probe used the wrong instrument.** In a category with no agreed
vocabulary, searching for complaints and purchases under-reports by
construction: nobody complains in terms you can search for, and nobody buys a
product category that doesn't exist yet. Payment lags vocabulary.

**Probe 2 — revealed preference.** Replaced "who complains" with **"who built a
workaround"**, and specifically: has any workaround ever crossed a *person
boundary*? Building costs real effort, so it's stronger evidence than
complaining and arrives earlier than purchasing.

The test was pre-registered before the result was known: *if nobody built a
cross-person version while dozens built the solo version, the absence is real
and we stop.*

## 02 · What the second probe found

Cross-person tooling **does** exist — at three tiers, none of them encouraging.

| Tier | Who | Adoption |
|---|---|---|
| **Vendor-native** | Anthropic Claude Code Team/Enterprise analytics (per-seat usage, spend, leaderboards); Cursor team analytics; GitHub Copilot metrics API | Shipped, bundled, free with an existing paid plan |
| **Commercial** | Jellyfish ("Autonomous Agent Activity" per developer), minware, Torii, Portkey, Mavvrik, Worklytics | Live products; all adoption claims vendor-published, none independently confirmed |
| **Practitioner OSS** | `m-shirt/claude-code-tracker` (28★/3 forks) · `ofershap/cursor-usage-tracker` (32★/12) · `ratneshpkn/tokenmaxxer` (0★, actively developed) · Copilot metrics dashboards (636★/322 forks) | Tens of stars, except the Copilot dashboards which sit on a vendor API |

**The asymmetry is the finding.** Solo agent-visibility tools attract thousands
of stars. The cross-person versions of the same idea attract tens. That is not
absence of demand — it is *weak* demand, squeezed from above by free vendor
features and from the side by DevEx platforms selling the manager-facing view.

## 03 · The gap that's left, and why we're not taking it

Everything cross-person stops at cost, tokens and counts. **Nobody does across
several people what `JKershaw/dash` does for one** — read actual agent
transcripts for friction and behaviour.

That is a genuine, identifiable gap. We are not filling it, for two reasons:

1. **It requires central collection of colleagues' transcripts.** That directly
   contradicts principle #1 (local-first, no accounts, no telemetry, nothing
   leaves the machine). Not a compromise — an inversion.
2. **It is a surveillance product.** The buyer is a manager; the subject is a
   developer. Jellyfish's per-developer agent-activity leaderboard already
   occupies that position. Developers resent being on the receiving end of it,
   and Orrery's whole credibility rests on being read-only and on the
   developer's side.

An empty space isn't automatically an opportunity. This one is empty partly
because of what filling it costs.

## 04 · Corrections to earlier research

Two claims from `DEMAND-VALIDATION.md` (July 2026) no longer hold:

- **"Orrery — nearly alone" in the watch-agents-you-use lane.** Out of date.
  `opcode`, `claude-usage`, `dash`, `claude-code-analytics` and assorted
  personal dashboards all read the same Claude Code JSONL. Orrery remains
  differentiated — multi-repo, live git state, Cursor as well as Claude, human
  context per project — but the lane is no longer empty and we should stop
  saying it is.
- **The Faros / LinearB review-bottleneck figures now have non-vendor
  corroboration.** Google's DORA research describes the same "verification tax"
  independently, and Stack Overflow's survey puts developer trust in AI accuracy
  at 29–33%. The July caveat about vendor-flavoured statistics can be relaxed
  for this specific finding.

## 05 · Two methodology notes worth keeping

**"Team dashboard" usually means *agent* team, not *human* team.** The
highest-starred apparent hit in the search (`mukul975/claude-team-dashboard`,
63★) turned out to be one person watching their own agent swarm. This vocabulary
collision is probably why the first probe read the space as empty. Anyone
researching this space again should assume "team" is ambiguous until checked.

**Research agents state wrong things confidently.** Probe 1 reported that
GitHub's Agent HQ shipped in March 2026 and was free with GitHub Enterprise.
Verified by hand: it was announced 28 October 2025 at GitHub Universe, and it's
bundled into **paid Copilot subscriptions** ($10–39/user/month) with each agent
session consuming a premium request plus Actions minutes. Both errors were on
the single most decision-relevant fact in the report. Verify the load-bearing
claim before acting on it.

---

## What would reverse this decision

Written as falsifiable checks, so re-opening the question is cheap:

1. **A well-adopted cross-person tool appears** — hundreds of forks, not just
   stars — doing deep multi-developer session or transcript analysis rather than
   cost dashboards. Currently the best example has 3 forks.
2. **A platform-engineering team publishes an internal rollout** of agent-
   activity visibility across their developers, with real usage numbers rather
   than a marketing page. None found.
3. **A buyer emerges who is not a manager** — evidence that developers
   themselves want and would pay for cross-team agent visibility, which would
   defuse the surveillance objection and create a constituency the vendors
   aren't already serving.

## Where this leaves Orrery

Single-player, local, cross-tool, free. The two probes independently re-confirm
the July recommendation: the pull is in the solo case, and the money in this
broader market is in **review and trust** — what shipped without review, what
was tested, what did this agent actually change.

That intersection — the thing developers pull toward, angled at the pain that
has proven willingness-to-pay — remains the position. Teams are not the
expansion path. Revisit only against the three checks above.

---

## Sources

**Vendor-native team analytics** —
[Claude Code analytics](https://code.claude.com/docs/en/analytics) ·
[Claude Team/Enterprise usage](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans) ·
[Cursor team analytics](https://docs.cursor.com/en/account/teams/analytics) ·
[GitHub Agent HQ announcement](https://github.blog/news-insights/company-news/welcome-home-agents/)

**Cross-person practitioner tooling** —
[m-shirt/claude-code-tracker](https://github.com/m-shirt/claude-code-tracker) ·
[ofershap/cursor-usage-tracker](https://github.com/ofershap/cursor-usage-tracker) ·
[ratneshpkn/tokenmaxxer](https://github.com/ratneshpkn/tokenmaxxer) ·
[microsoft/copilot-metrics-dashboard](https://github.com/microsoft/copilot-metrics-dashboard) ·
[copilot-metrics-viewer](https://github.com/github-copilot-resources/copilot-metrics-viewer)

**Solo tooling (the comparison set)** —
[phuryn/claude-usage](https://github.com/phuryn/claude-usage) ·
[JKershaw/dash](https://github.com/JKershaw/dash) ·
[winfunc/opcode](https://github.com/winfunc/opcode) ·
["I built a real-time dashboard because I kept losing track of my sessions"](https://dev.to/slima4/i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions-2m54)

**Commercial layer** —
[Jellyfish Claude Code dashboard](https://jellyfish.co/platform/claude-code-dashboard/) ·
[Jellyfish Cursor dashboard](https://jellyfish.co/platform/cursor-dashboard/) ·
[builderz-labs/mission-control](https://github.com/builderz-labs/mission-control)

**Review bottleneck / spend governance** —
[DORA](https://dora.dev/insights/balancing-ai-tensions/) ·
[Stack Overflow trust gap](https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/) ·
[Faros AI](https://www.faros.ai/blog/ai-software-engineering) ·
[LinearB 8.1M PRs](https://linearb.io/blog/8-million-prs-engineering-productivity) ·
[FinOps Foundation 2026](https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1)

---

*Caveat: adoption claims from commercial vendors (Jellyfish, minware, Torii,
Portkey and the rest) are vendor-published with no third-party confirmation, and
should be read as evidence of positioning rather than of traction. GitHub star
and fork counts were pulled live and are the most reliable numbers here. The
strongest single data point in this document — 28 stars on a working
multi-user Claude Code dashboard — is one observation, not a market study; it is
load-bearing because it points the same way as everything else, not on its own.*
