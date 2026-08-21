# Where can Prima make money in agent tooling?

**Research report — 2026-08-10.** Four research probes, key claims verified by
hand. Two candidate directions tested. Both rejected as stated. One narrow
survivor identified, with three cheap tests to settle it.

---

# PM SUMMARY

## BLUF

Neither direction we tested is worth building as scoped. **Orrery should not
become a team product** — someone already shipped that exact product and it has
28 stars while solo equivalents have thousands, and Anthropic, Cursor and GitHub
now all ship team dashboards free inside plans teams already buy. **Agent cost
attribution ("agent FinOps") is not greenfield** — Datadog already ingests AI
cost from eight providers including GitHub Copilot and Cursor, with per-user
allocation, inside a contract the buyer has already signed and security-reviewed.
The underlying pain is real and well-evidenced (Anthropic's own docs put
enterprise Claude Code at $150–250/dev/month against a $20 seat), but the
category formed in 2025 and the enterprise segment that holds the money is
unreachable for a solo operator — $25–50k and 6–12 months for SOC 2 alone
against a comparable charging $180/year. **One genuinely unserved gap survives**:
cost attributed to a work object (ticket, PR, repo) plus the model-mix
counterfactual, which no vendor, gateway or FinOps incumbent claims to answer.

## Signals

| | Signal | So what |
|---|---|---|
| 🔴 | Someone built the team Orrery: 28★, 3 forks. Solo equivalents: thousands | The experiment ran; nobody came |
| 🔴 | Datadog AI Costs covers Bedrock, Anthropic, Gemini, OpenAI, Vertex, **Copilot, Cursor** with per-user allocation | The "empty square" is occupied by an incumbent already under contract |
| 🟠 | FinOps practitioners managing AI spend: 31% (2024) → 63% (2025) → **98% (2026)** | The category-founding window closed in 2025 |
| 🟠 | Anthropic ships a free self-hosted gateway with 429-enforced per-user spend caps, inside the `claude` binary | The model vendor is competing in the category directly |
| 🟠 | Lineman: 4-month-old sole-director company, 978 npm/wk vs ccusage's 83,521, zero customers, zero HN mentions ever | The proof-point the thesis leaned on isn't one |
| 🟢 | Spend genuinely is variable: $150–250/dev/mo against a $20 seat, 12.5x median-to-power-user spread | The pain is real, whatever we build |
| 🔵 | Nobody attributes cost to a ticket, PR or repo. Cursor's own research: **8x cost spread for equal quality** | The one gap worth anything |

## Top findings

- **The team direction is closed by adoption, not by product quality.**
  `m-shirt/claude-code-tracker` does exactly what a team Orrery would — syncs
  every teammate's `~/.claude/` centrally, RBAC and all — at 28 stars, 3 forks.
- **The FinOps direction is closed by incumbency.** Datadog shipped the
  cross-vendor per-user square. Flexera launched a competitor at FinOps X in
  June. Vantage and CloudZero ingest Anthropic directly. Anthropic's own admin
  launch shipped *with prebuilt Datadog and CloudZero integrations*.
- **The enterprise reframe was right about the money and wrong about
  reachability.** Compliance is $25–50k and 6–12 months before the first
  questionnaire can be answered; procurement is 6–9 months with a ~$25–50k ACV
  floor; the comparable charges $14.99–$49.99/month.
- **The free incumbent sets the floor at zero and owns the distribution.**
  ccusage: MIT, 16 agents, 83,521 npm downloads/week, committed daily. Lineman
  pays affiliate commission to funnel ccusage's users — the category's best
  channel is already bought, for less than the price of a Max subscription.
- **One thing nobody does:** attribute cost to a ticket, PR or repo, or tell you
  which model mix you should have used. Practitioners name it unprompted:
  *"Most token trackers just tell you total spend. This tells you what kind of
  work the spend went to."*

## What would change this view

1. Lineman turns out to have real paying customers at volume — settled for $15
   and one email (see Tests, below).
2. A cross-person or per-work-object tool appears with real adoption (hundreds
   of forks, not stars), showing the demand exists where we found none.
3. Evidence that engineering leads actually ask "what did this ticket cost" —
   currently a 900-person practitioner survey shows zero such requests and
   universal use of spend *caps* instead.

## Confidence

**Solid** — vendor pricing and native capabilities (fetched from vendor docs);
Microsoft's FY26 Q4 quotes (official transcript); Anthropic's per-developer cost
benchmarks; ccusage and Lineman adoption (GitHub API, npm registry, Companies
House, HN Algolia queried directly); Datadog's provider list (verified by hand
after the report landed); FinOps Foundation survey data.

**Weak** — procurement cycle lengths and ACV thresholds (lead-gen content sites
citing each other); compliance platform pricing (Vanta, Drata and Secureframe
all publish zero dollar figures, so every cost estimate comes from their
competitors); first-year revenue for a solo enterprise vendor (no dataset
exists).

**Not examined** — Reddit was hard-blocked across five access methods.
r/ClaudeAI, r/cursor and r/ExperiencedDevs are a genuine gap.

---

# DEPTH

## 01 · What we asked

Two questions, in sequence, each gated on the last.

**Should Orrery become a team product?** Four surfaces already exist for the solo
case — Sessions, Worktrees, Work Log, Skills. Teams were the obvious expansion.

**If not, where else in agent tooling can a small operation charge money?** Which
became a specific thesis worth testing on its own: agent spend went variable in
2026, nobody can see it, and that's a place to launch.

## 02 · The team product — closed

**The decisive fact.** `m-shirt/claude-code-tracker` is a self-hosted, multi-user
Claude Code analytics dashboard — syncs every teammate's `~/.claude/` to a
central server, role-based access, admins see everyone. **28 stars, 3 forks.**
Solo tools reading the same files get thousands. The experiment has been run.

**Above it, the vendors give it away.** Anthropic ships Claude Code
Team/Enterprise analytics — per-seat usage, spend, leaderboards, CSV and OTel
export. Cursor ships team usage analytics. GitHub ships Copilot metrics plus
Agent HQ. All bundled into plans the target buyer already pays for.

**Beside it, the commercial middle is taken.** Jellyfish sells a Claude Code
dashboard with an explicit per-developer "Autonomous Agent Activity" metric.
minware, Torii, Portkey and Mavvrik sell per-engineer attribution.

**And the one gap left is a surveillance product.** Everything cross-person stops
at cost and counts; nobody reads *multiple developers' transcripts* for
behaviour. Filling that means centrally collecting colleagues' agent
conversations — an inversion of Orrery's local-first promise, sold to a manager
about a developer. That space may be empty because of what filling it costs.

*Full decision record: [`TEAM-COLLAB-RESEARCH.md`](TEAM-COLLAB-RESEARCH.md).*

## 03 · Agent FinOps — closed as stated

### The pain is real

Anthropic publishes it themselves: *"around $13 per developer per active day and
$150-250 per developer per month"* — against a $20 seat. OpenAI's Codex rate card
says *"~$100-$200/developer per month."* **Roughly 75–90% of true cost is metered
consumption.** GitHub's own rationale for repricing on 1 June 2026:
*"a quick chat question and a multi-hour autonomous coding session can cost the
user the same amount."*

Dispersion is severe. Anthropic's docs show median $40, mean $215, power users
$500 — a 12.5x spread. Ramp's card data across 70,000 businesses: median firm
$11.38 per employee per month, top decile $611, top 1% $7,450.

### But the category already formed

FinOps practitioners managing AI spend went **31% (2024) → 63% (2025) → 98%
(2026)** on a survey of 1,192 respondents. The FinOps Foundation made "FinOps for
AI" a formal technology category in March 2026 and rewrote its mission from
"Value of Cloud" to "Value of Technology."

The cloud precedent says this took twelve years last time — EC2 in 2006, first
$100M+ exit in 2018. AI spend compressed the same arc into about two years,
because it inherited the foundation, the framework, the job title and the buyer
fully formed.

### And the square is occupied

**Datadog AI Costs** ingests from Amazon Bedrock, Anthropic, Google Gemini,
OpenAI, Vertex AI, **GitHub Copilot and Cursor**, with out-of-the-box allocation
rules attributing to users and API keys, and tag pipelines mapping to teams and
business units. *(Verified by hand at `docs.datadoghq.com/cloud_cost_management/ai_costs/`.)*

That is cross-vendor × whole-team, per-user, shipped — inside a product the
target buyer already has under contract, already security-reviewed, already
renewing. Flexera launched a competing product at FinOps X in June. Vantage and
CloudZero ingest Anthropic directly. Anthropic's own admin-visibility launch
shipped *with prebuilt Datadog and CloudZero integrations*.

### The natives closed the obvious gaps in ten weeks

Between 29 May and 7 August 2026, GitHub shipped ten separate spend-visibility
features — usage-based billing GA, user-level budgets, `ai_credits_used` per
user, cost-centre credit pools, repository-level metrics, an ROI dashboard.
Anthropic shipped an Enterprise Analytics API, a Spend Limits API with per-member
caps and an approval queue, and admin visibility with threshold alerts. Cursor
shipped soft limits and per-user filtering.

**And Anthropic ships its own gateway.** `claude gateway` — self-hosted, inside
the CLI binary, OIDC SSO so developers hold no API keys, routes to Bedrock /
Vertex / Foundry / the API, fans OTLP telemetry to Datadog or Splunk, and
enforces per-user and per-group spend limits with a hard HTTP 429. It bills
aborted requests against a token floor so you can't abort-to-evade. The data
plane deliberately sends nothing to Anthropic unless the Anthropic API is a
configured upstream.

### The proof-point isn't one

The thesis leaned on Lineman.io as evidence someone will pay. What it actually
is: **Goo Holdings Ltd, incorporated 7 April 2026, one director, registered to a
residential address, one filing ever.** Product shipped 28 May. `/about`,
`/team`, `/careers` all 404.

- **978 npm downloads/week** against ccusage's **83,521** — 1.2%, for a product
  covering one agent against ccusage's sixteen.
- Zero named customers. Site figures captioned *"Illustrative figures from a
  synthetic example team, not a customer account."*
- **Zero Hacker News mentions, ever** (HN Algolia, nbHits: 0).
- SOC 2 Type II, ISO 27001 and ISO 27701 all *"In progress"* — no certificate
  exists. To their credit they say so plainly.
- Their own `/benchmarks` page reports their headline token-saving feature
  performing **20.9% worse on cost** than baseline.
- Pricing is not "flat unlimited" as first reported: $14.99/mo capped at $500
  tracked spend, $49.99 Pro at $1,000. Unlimited *seats*, metered *spend*.

**No verified evidence was found that anyone pays for any Claude-Code-specific
cost tracker.** That is the single most important null in this research.

### The enterprise reframe made it harder, not easier

Correct about where the money is. Fatal on reachability:

| Gate | Cost |
|---|---|
| SOC 2 Type II | $25–50k cash, **6–12 months** before the first questionnaire can be answered |
| ISO 27001 + 27701 | +$20–35k year one, $8–12k/yr thereafter |
| Procurement | 6–9 months, 6–10 stakeholders, CFO gate above ~$50k |
| Soft ACV floor to justify the cycle | $25k arguable, $50k+ to clearly pay |
| The comparable's price | **$180/year** |

That's a factor of 150, not a positioning problem. And ISO's
segregation-of-duties expectations imply roughly nine non-overlapping roles —
structurally impossible for one person, not merely expensive.

## 04 · What survived

**Two claims stood up.**

*Spend went variable and the pain scales.* Well-evidenced above.

*It rises with adoption.* Alphabet went 16B → 22B tokens/minute in a quarter.
Microsoft: Copilot revenue *"accelerated over 60% quarter-over-quarter"* after
the June repricing, 50 million Copilot users, one in three GitHub PRs now
involving an agent.

**One counter-signal worth carrying:** Atlassian disclosed that agents grounded
in their Teamwork Graph produce *"44% more accurate answers while consuming 48%
fewer tokens,"* and that heavy users *"are spending less on tokens than their
peers for equivalent work."* Efficiency pushes against volume. And GitLab's ~$20M
consumption run-rate arrived alongside seat contraction and a 14% workforce
reduction — consumption may be substituting for seat revenue rather than adding
to it.

**And one genuine gap.** Nobody — no vendor console, no gateway, no FinOps
incumbent — attributes cost to a **work object** (ticket, PR, repo) or answers
the **counterfactual**: which model mix should you have used? Cursor's own
research found that on the same task, *"Every mix produced similar quality, but
the costs varied enormously"* — **$1,339 to $10,565, an 8x spread.**

Practitioners name it unprompted. The most-upvoted comment on a Show HN for a
token tracker: *"Most token trackers just tell you total spend. This tells you
what kind of work the spend went to."*

### If Prima built anything

- **Product:** per-PR and per-ticket cost, cross-vendor, plus a model-mix
  recommendation with a measured counterfactual. An answer, not a dashboard.
- **Segment:** engineering leads at 10–200 developers. **Explicitly not
  enterprise** — below the procurement line, above the hobbyist line.
- **Price:** $200–1,000/month per team, self-serve, credit card. Infracost's
  ladder, not Lineman's.
- **Ingestion:** metadata-only, via provider Admin APIs and local logs. Never
  prompt bodies. Anthropic's usage APIs return token counts and opaque IDs with
  no prompt text anywhere — that boundary plausibly moves a vendor from full
  InfoSec review to a light one, and it should be a stated product boundary.
- **Day one:** point it at a repo; it labels the last 30 days of merged PRs with
  what each cost across Claude Code and Cursor, and flags the five that cost more
  than they should have.
- **Smallest payable version:** a weekly *"your five most expensive PRs, and the
  cheaper mix that would have worked"* email.
- **Don't call it FinOps.** The moment it's FinOps, it lands in a category where
  the buyer already has a vendor.

**Honest odds:** the wedge is real, the market is small, the buyer is a VP Eng
with discretionary budget rather than a FinOps function, and Datadog can add
PR-level attribution whenever it becomes interesting. Better than the stated
thesis. Not obviously good.

## 05 · Three cheap tests

**1. Buy Lineman for a month and email the founder. $15.**
Support, sales and billing reach the same inbox and he answers fast during beta.
Ask how many paying teams he has. A four-month-old sole trader will usually tell
you. Under twenty and the seam is unproven and this is finished. Highest
information per pound available; do it before anything else.

**2. Post the counterfactual, not the dashboard. One weekend.**
Take twenty merged PRs from a real repo, compute what each cost across Claude
Code and Cursor, identify the five run on the wrong model mix and what the
cheaper mix would have cost, publish it. Measure whether it lands differently
from every other token-tracker post, and specifically whether an engineering lead
at a 10–200-person team asks for it against their own repo. Orrery already has
the parsers.

**3. Ask ten engineering leads one question. Ten emails.**
Not "would you pay for spend visibility" — nobody answers that honestly. Ask:
*"Last quarter, did anyone ask you what a specific ticket or PR cost in AI spend?
What did you do?"* Count real requests versus caps-set-and-forgotten. A
900-person practitioner survey suggests the answer is zero real requests and
universal caps. Ten replies tell you whether that generalises.

## 06 · Corrections to earlier research

Things this work overturned, including things stated earlier in this project:

- **"Orrery is nearly alone in the local lane"** (July scan) — dead. `opcode`,
  `claude-usage`, `dash`, `claude-code-analytics` and assorted personal
  dashboards all read the same Claude Code JSONL. Orrery is still differentiated
  (multi-repo, live git state, Cursor as well as Claude, human context) but the
  lane has traffic.
- **The Faros/LinearB review-bottleneck figures** now have non-vendor
  corroboration — DORA's "verification tax," Stack Overflow's trust decline to
  29–33%. That July caveat can be relaxed for this specific finding.
- **CodeRabbit's $40M ARR** — unverifiable. Traces to a Sacra *estimate*, not a
  company statement. Do not reuse.
- **Claude Code's $1B and $2.5B run-rates ARE real** and first-party (Anthropic's
  own news post and Series G announcement). Only the **$8B is fabricated** — it
  is attributed by aggregators to a Series H post that contains no Claude Code
  revenue figure at all. The fake travels because its neighbours are genuine.
- **"98% of organisations manage AI spend"** — real and primary, but it means 98%
  of *FinOps practitioners*, not organisations. The corrected version is worse
  for the thesis, not better.
- **GitHub Agent HQ** — announced **28 October 2025**, not March 2026, and
  bundled into **paid Copilot subscriptions** ($10–39/user/month with metered
  premium requests), not free with Enterprise.

## 07 · Method notes worth keeping

**Search workarounds, not complaints.** The first probe asked whether teams
complain and whether anyone pays; both came back empty. In a category with no
agreed vocabulary that under-reports by construction — you can't search for an
unnamed problem, and you can't buy a category that doesn't exist. Searching the
*artefact* instead ("I built X because Y") found the pain immediately, stated in
practitioners' own words.

**"Team dashboard" usually means *agent* team, not *human* team.** The
highest-starred apparent hit in the team search was one person watching their own
agent swarm. That vocabulary collision is probably why the first probe read the
space as empty.

**Research agents state wrong things confidently.** One probe reported GitHub's
Agent HQ as shipping March 2026, free with Enterprise — wrong on both counts, on
the single most decision-relevant fact in its report. Another laundered a Sacra
estimate into a market size. The fix that worked: a three-tier evidence contract
(`[VERIFIED]` = primary source fetched, with URL and date; `[REPORTED]` = name
the chain; `[UNVERIFIABLE]` = say so), a structural expectation that prices are
verifiable and private ARR is not, and a mandatory "numbers I could not stand up"
section that isn't allowed to be empty. Load-bearing claims still get checked by
hand.

---

## Sources

**Verified by hand after the research landed** —
[Datadog AI Costs](https://docs.datadoghq.com/cloud_cost_management/ai_costs/) ·
[GitHub Agent HQ](https://github.blog/news-insights/company-news/welcome-home-agents/) ·
[Lineman.io](https://lineman.io) · [ccusage](https://github.com/ccusage/ccusage)

**Vendor pricing and docs** —
[Claude Code costs](https://code.claude.com/docs/en/costs) ·
[Claude pricing](https://claude.com/pricing) ·
[Claude Code analytics](https://code.claude.com/docs/en/analytics) ·
[Cursor pricing](https://cursor.com/pricing) ·
[Cursor team analytics](https://docs.cursor.com/en/account/teams/analytics) ·
[Copilot plans](https://github.com/features/copilot/plans)

**Competitive** —
[m-shirt/claude-code-tracker](https://github.com/m-shirt/claude-code-tracker) ·
[Jellyfish Claude Code dashboard](https://jellyfish.co/platform/claude-code-dashboard/) ·
[builderz-labs/mission-control](https://github.com/builderz-labs/mission-control) ·
[phuryn/claude-usage](https://github.com/phuryn/claude-usage) ·
[JKershaw/dash](https://github.com/JKershaw/dash) ·
[winfunc/opcode](https://github.com/winfunc/opcode)

**Market and precedent** —
[FinOps Foundation survey data](https://data.finops.org) ·
[FinOps tools and services](https://finops.org/wg/finops-tools-and-services/) ·
[DORA](https://dora.dev/insights/balancing-ai-tensions/) ·
[Stack Overflow trust gap](https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/) ·
[AWS Marketplace fees](https://docs.aws.amazon.com/marketplace/latest/userguide/listing-fees.html)

---

*Caveat: this is a lean research programme, not an exhaustive market study. The
strongest evidence here is vendor pricing and adoption metrics, all fetched from
primary sources. The weakest is anything about procurement economics, where every
number traces to sales-benchmark content sites citing each other — treat those
directionally. Reddit was inaccessible throughout, which leaves the largest
practitioner communities unexamined. And the single most load-bearing null —
that nobody was found paying for a Claude-Code-specific cost tracker — is an
absence of found evidence, which is weaker than evidence of absence. Test 1
exists to convert it.*
