# Who's actually paying, in AI dev tools?

**Market money map — August 2026.** Where willingness-to-pay demonstrably sits,
what it means for a free local developer tool, and which circulating figures are
fabricated.

*2026-08-20 · one commissioned probe plus findings carried from the multiplayer
run. Load-bearing numbers re-verified by hand; confidence marked per claim.*

> **Partial by construction.** The harness category is verified and locked. Seven
> further category probes were still running when the run's web-search budget was
> exhausted — code review, engineering analytics, FinOps, observability, security
> and testing are covered here from the *earlier* multiplayer probes, not from
> fresh verification. Marked accordingly.

---

## Bottom line

**The money is in the harness seat, and it is not close.** Everything else in this
market — review bots, analytics, spend governance, provenance — is a rounding
error next to what people pay for the agent itself.

Two facts reframe the picture:

1. **Individuals appear to pay at scale — but the number is softer than it looks.**
   At $2B annualized, ~40% of Cursor's revenue came from "individuals and small
   startups," which reads as ~$800M/yr of out-of-pocket spend. **Treat that with
   caution.** A recurring pattern in practitioner reports is *"we're on personal
   plans linked to corporate e-mail and company credit cards"* — consumer-tier
   SKUs absorbing corporate spend. Any vendor's individual-vs-enterprise split
   likely overstates the individual side. See §06 for why no better number exists.
2. **But the centre of gravity is moving to enterprise, fast.** Cursor was ~60%
   corporate at $2B. Anthropic says enterprise is now *"over half of all Claude
   Code revenue."* Both crossed that line within the last year.

For a free, local, no-telemetry tool, the uncomfortable part isn't that developers
won't pay. It's that **the one thing they reliably pay for is the harness — and
the harness vendors own it.**

---

## 01 · The harnesses — verified

| Company | Figure | Confidence |
|---|---|---|
| **Cursor / Anysphere** | **Acquired by SpaceX. Effective 2026-08-14**, shares converted into **389,289,254** SpaceX Class A shares *"based on an implied equity value of Cursor of $60.0 billion."* | ✅ **Verified in the SEC Form 8-K, Item 2.01** — not a press release |
| Cursor revenue | ~$2B annualized, **~60% corporate / ~40% individual** | ✅ Verified — TechCrunch citing Bloomberg, 2026-03-02 |
| Cursor valuation ladder | $9.9B (Jun 2025, ~$500M ARR) → $29.3B (Nov 2025) → $50B talks (Apr 2026) → $60B exit | 🟡 Probe-reported |
| **Claude Code** | **>$2.5B run-rate**, *"more than doubled since the beginning of 2026"*; *"enterprise use has grown to represent over half of all Claude Code revenue"* | ✅ Verified — anthropic.com Series G announcement (vendor, but primary) |
| Anthropic Series G | $30B raised at $380B post-money | ✅ Verified — same |
| **GitHub Copilot** | 50M *users*; revenue *"accelerated over 60% quarter-over-quarter"*; usage-based billing introduced | 🟡 Probe-reported — Microsoft FY26 Q4 call |
| **Cognition** (Devin + Windsurf) | $492M run-rate; $1B raise at $25B pre-money (May 2026); reportedly in talks at $40B | 🟡 Probe-reported, company-stated |

**Verified pricing:** Cursor Pro $20 / Pro+ $60 / Ultra $200 / Teams $40 per user /
Teams Premium $120. Copilot Free / Pro $10 / Pro+ $39 / Max $100. Claude Pro $20 /
Max $100+ / Team $25 per seat.

### Two reading notes worth keeping

**Microsoft's disclosure is deliberately asymmetric.** They report "over 30 million
**paid** Microsoft 365 Copilot seats" but only "50 million **users**" for GitHub
Copilot. Read the 50M as including the free tier.

**Cursor's India-only ₹649 tier** is a tell: they were defending individual share
in price-sensitive markets right up to the acquisition.

### Fabricated figures to reject

- **"Codex $2.5B run-rate"** — a conflation with Claude Code's identical figure
  from the same month. **OpenAI does not break out Codex revenue.** Treat it as an
  honest empty; the only public numbers are user counts.
- **Anthropic's company-wide run-rate reported as "Claude Code revenue"** — several
  SEO farms garbled this. Different number, different scope.
- **"$420M AI-code-review category ARR"** — **traced to a single uncited blog post
  and fails a sanity check by 4–8×.** Full provenance in §02. This figure is
  currently flagged 🟢 Strong in
  [`TEAM-COLLAB-RESEARCH.md`](TEAM-COLLAB-RESEARCH.md) and **should be struck, not
  downgraded.**
- **"SonarQube $430M+ ARR"** — falsely attributed to a Sonar press release that
  contains no revenue figure at all.
- **"CodeRabbit $40M ARR, April 2026"** — a misattribution of Sacra's ~$50M/July
  estimate. This file repeated it before catching it.
- **"$200–$500 per developer per month on AI coding (25% of tech leaders)" and
  "$2,000+ (6%)"** — widely attributed to Gartner's June 2026 release. A full-text
  check found that release contains **no dollar figures and no survey data at
  all**. The numbers trace to a separate, unnamed Gartner artifact with unknown
  sample and methodology. Tempting and quotable; don't use without the underlying
  paywalled document.

This topic is unusually contaminated. Search returns a whole tier of sites
(getpanto, serpsculpt, orbilontech, taskade and similar) recycling each other's
errors. Anything not traced to a filing, a funding announcement, or a named
publication should be assumed wrong.

---

## 02 · Engineering-management analytics — verified

The one non-harness category that got a full pass. It's the closest adjacent
market to Orrery, and its economics are worth reading carefully.

**The category's defining event is an exit, not a funding wave.**

| Fact | Confidence |
|---|---|
| **Atlassian acquired DX for $1B** in cash + restricted stock, announced 2025-09-18, closed Nov 2025 — **on under $5M of venture funding** | ✅ Verified — TechCrunch |
| Atlassian's CEO framed it as AI spend justification: *"You suddenly have these budgets that are going up… Am I spending the money in the right ways?"* | ✅ Verified — same |
| **Harness** $240M Series E Dec 2025 at $5.5B post (up round), >$250M ARR | 🟡 Probe-reported, multiple outlets |
| **Jellyfish** has not raised since **Feb 2022**. **Faros AI** not since **June 2023** | 🟡 Probe-reported |

**Median contract values** (Vendr verified-purchase data — ordering is more
reliable than the absolute figures, which move): DX ~$53.7k · Jellyfish ~$57.5k ·
LinearB ~$25.9k · Swarmia ~$14.7k.

**Category health is poor underneath the DX headline.** Pluralsight Flow (bought as
GitPrime for $170M in 2019) was sold to Appfire in Feb 2025 and **retires
2027-12-31** — its renewal window already closed on 2026-06-30. Code Climate spun
Quality out into a separate company. Sleuth pivoted out of measurement entirely
into AI-agent governance. The two purest AI-ROI plays haven't raised in 3–4 years.

**The pitch converts for strategic acquirers, not for independents.** Atlassian
paid ~15–20× estimated ARR because it owns the install base. Standalone vendors
selling the same thesis are flat.

### Runtime agent observability — the category consolidated, hard

⚠️ Still a different market from ours — this is tooling for LLM apps *companies
ship to their own users*, not coding agents developers use. Included because the
shape is instructive.

**Six of twelve pure-plays were acquired inside twelve months:** Arize →
Dynatrace (**$915M**, Aug 2026), Weights & Biases → CoreWeave (**$1.03B**),
Langfuse → ClickHouse, Galileo → Cisco/Splunk, Helicone → Mintlify, Traceloop →
ServiceNow (~$60–80M), plus Humanloop acqui-hired by Anthropic with its platform
shut down entirely.

**Two corrections worth carrying:**

- The widely-repeated **"$1.7B" for Weights & Biases is wrong.** CoreWeave's own
  10-Q puts aggregate consideration at **$1.029B**; the $1.7B came from pre-close
  reporting at an expected IPO share price. 🟡 Probe-read from the filing.
- I earlier wrote "**Braintrust** $80M Series B at $800M." The round and lead
  (ICONIQ, Feb 2026) are solid; **Braintrust's own announcement disclosed no
  valuation** — the $800M is press-reported. Soften accordingly.

**And the tell: essentially none of these companies has a public ARR figure.**
Not Braintrust, Arize pre-deal, Galileo, Patronus, HoneyHive or Langfuse. Growth
gets published as multiples with no base — "834% growth," "15x" — which is what
you publish when the base is small. The Information ran a piece titled *"Revenue
Lags at AI Evaluation Startups."*

Money is now flowing to **general observability platforms adding AI** (Coralogix
$200M, groundcover $100M) rather than to pure-play evaluation startups. Same
pattern as every other category here: the independent middle gets bought or dies.
| **IP / licence audit** | Black Duck, SCANOSS, FOSSA | 20-year-old M&A due-diligence work with an AI inflow, not a new category. |

### AI code review — verified, and the $420M is traced

**The category is real and funded.** Verified:

| Fact | Confidence |
|---|---|
| **CodeRabbit — $143M Series C at $1.5B post, 2026-08-12**, co-led by Atomico and Smash Capital (Datadog and BMW i Ventures participating). *"Revenue grew more than 5x year-over-year"* — no absolute figure disclosed | ✅ Verified |
| CodeRabbit ARR ~**$50M (July 2026)** | 🟠 Sacra **estimate**, explicitly labelled as such — not a disclosure |
| CodeRabbit pricing: Pro **$24**/user/mo, Pro Plus **$48**; free forever for public OSS | ✅ Verified on their page |
| **Qodo** — $70M Series B (2026-03-30, Qumra), $120M total; ARR $1M → $10M per company | 🟡 Funding verified; ARR vendor-published |
| **Greptile** — $25M Series A led by Benchmark; $30M cumulative. ARR: founder says only *"millions"* | 🟡 Probe-reported |
| **Graphite** acquired by Cursor 2025-12-19; **Gitar** acquired by Sonar 2026-05-21 | 🟡 Both prices undisclosed |
| **GitHub Copilot: ~1 in 5 reviews on GitHub** now comes from Copilot; 60M reviews processed | 🟠 Secondary source only |

That last row is the one that should worry the pure-plays: the incumbent bundles
review into a $10/mo subscription and already touches a fifth of all reviews.

**Now the $420M figure — traced to origin and it's fabricated.**

It comes from a single content-marketing blog post (IdeaPlan, 2026-05-07):
*"Estimated 2026 ARR across pure-play vendors is ~$420M, up from roughly $180M in
2025."* ✅ I fetched the page. **It cites nothing.** Every outbound link is
internal; no Gartner, Forrester, IDC, CB Insights or Sacra reference appears
anywhere. The page's own boilerplate claims *"We cite our sources inline and
disclose our methodology"* — while citing no source for this number. One
downstream site repeats it, also uncited. Two nodes, no primary source at either
end.

**And it fails a sanity check.** Sum the visible pure-plays — CodeRabbit ~$50M
(estimate), Qodo $10M, Greptile "millions," everyone else seed-stage — and you get
**under $100M**. $420M would require the category to be four to eight times the
sum of its own named leaders.

**No defensible category size exists.** No Gartner/Forrester/IDC standalone "AI
code review" forecast surfaced; CB Insights treats review as a *feature* of coding
AI, not a segment; a16z deliberately declines to size it. The only third-party
dataset with a stated methodology is YipitData (panel spend across 1,200+
companies), and it publishes ACVs and growth — not a TAM.

> **Correction to this file.** An earlier draft said *"CodeRabbit ~$40M ARR
> (Apr 2026), $143M Series B."* Wrong on all three: it's a **Series C**, and the
> "$40M / April 2026" figure is itself a laundered misattribution of Sacra's
> ~$50M/July estimate. I repeated a fabricated number inside a section warning
> about fabricated numbers. That is how contaminated this topic is.

### Code security — the split that explains everything

The cleanest natural experiment in the dataset. AI security money is real, but it
went somewhere specific:

**New budget — AI *runtime*/agent security.** ~$1.4B+ of disclosed strategic M&A in
18 months: Aim $350M (Cato), Lakera $300M (Check Point), Prompt Security $250M
(SentinelOne), CalypsoAI $180M (F5), AllTrue $150M (Varonis), Apex $105M+
(Tenable), plus Protect AI to Palo Alto at an estimated $650–700M. Zenity raised
$125M and Noma $100M. The buyers are network, endpoint and data-security vendors —
not AppSec.

**Relabelled budget — AI *code* security.** **Snyk is at ~$326M ARR growing 7%
YoY, down from 27%** — ✅ confirmed at Sacra as *their estimate*, not a disclosure.
Snyk did everything the AI thesis prescribes: AI-native SAST, an "AI Trust
Platform," an MCP-security acquisition. Growth still collapsed. GitLab decelerated
29%→23% and cut ~14% of staff.

> ⚠️ The probe also reported a "$7.4B → $3.7B BlackRock markdown." **Sacra does not
> corroborate that** — it gives $7.4B as the Dec 2022 round valuation and mentions
> no markdown. Don't cite the $3.7B without a better source.

**The sharpest single fact in the whole run:** *not one strategic acquirer paid a
premium for AI-generated-code scanning.* Every AI-security acquisition above was
"secure the AI the enterprise **uses**," never "scan the code the AI **writes**."
If scanning AI-written code created new budget, that gap wouldn't exist.

### SaaS spend management — a category with bodies in it

**Productiv raised $73M and ceased operations on 2026-08-06** — ✅ verified on their
own site: *"all production systems, data stores, and backups have been permanently
and securely destroyed,"* with creditors directed to an assignment for the benefit
of creditors. Two weeks ago. Torii cut 30% of staff in 2023.

Zylo and Torii both shipped AI-spend modules within five weeks of each other
(2026-04-14 and 2026-05-12). Neither publishes a price for it. Cledara — well
funded, transparently priced, publishes data showing AI is now **~10% of software
spend** — ships **no** AI governance SKU at all. Packaging, not pricing. Again.

**One stat here matters directly to Orrery:** a 396-org survey (Mavvrik/Benchmarkit,
fielded Apr–May 2026) found **98% of engineering orgs use AI coding assistants,
averaging 2.4 tools simultaneously.** That is independent support for the
cross-tool premise behind `multitool-sessions-plan.md` — people really do run more
than one agent vendor at once.

### AI spend governance — verified, and it's a negative

Seven vendors checked (Vantage, CloudZero, Finout, Cast AI, Kubecost/IBM,
Cloudability/Apptio, minware). **Not one sells AI cost management as a separate
SKU.** In every case it ships as a bundled capability inside the existing
platform.

What changed instead is the **pricing metric** — the denominator quietly widened:

> **Finout**: *"The FinOps platform for cloud and AI spend"*; fee banded by
> *"committed cloud and AI spend tier."* No separate AI SKU or add-on.
> ✅ Verified on their pricing page.
>
> **CloudZero**: single subscription sized to *"your AI **or** cloud
> environment."* Rebranded itself "The AI ROI Company" in May 2026 — and still
> created no priced AI product.
>
> **Vantage**: LLM Token Allocation is a tier-gated feature on Business/Enterprise,
> not a SKU. AI provider bills flow into the same tracked-spend total.

**Why that's the interesting part.** These vendors demonstrably know how to
unbundle — Cast AI sells a "$200/mo Cost Monitoring Add-on," Finout charges "+25%"
for extra integrations. They chose *not* to unbundle AI. That is the most direct
evidence available that **buyers do not yet hold a separate AI-governance budget**;
the vendors are capturing AI-spend upside through tier creep instead, with no new
sales motion and no new budget line at the customer.

**Correction to how this file first read the FinOps Foundation number.** I cited
"98% of practitioners now manage AI spend, up from 31%" as *"a budget line that
didn't exist, with a named owner."* That's a misreading. The figure is measured
**among FinOps practitioners** (n=1,192) — it says existing FinOps teams absorbed
AI into their remit. That is the absorption hypothesis stated as a statistic, not
evidence of a new budget line.

Everything else points the same way:

- **Gartner has not minted an AI-cost-management category.** It stayed inside
  *Cloud Financial Management Tools* — while Gartner *did* mint two brand-new AI
  categories in 2026 (AI SRE Tooling, AI Assistants for IaC). They're willing; they
  haven't.
- **Forrester argues explicitly for embedding over standalone**, and openly doubts
  the new Tokenomics Foundation is warranted.
- **IBM's Q2 2026 earnings call mentions "FinOps" zero times** — and IBM owns
  Apptio, the Gartner Leader in the category.
- **Job titles are adjectives on an existing function**: "AI FinOps," "Cloud & AI
  FinOps," "FinOps AI Governance Lead" — roughly 25–75 US postings against ~2,000
  for FinOps generally (~1.25%).

**The counter-evidence, and it's real:** the Linux Foundation launched the
**Tokenomics Foundation** on 2026-08-04 with ~30 founding members (Vantage, Finout,
Cast.ai, IBM, SAP, ServiceNow, JPMorganChase), a conference, and work to put token
cost telemetry into the FOCUS spec. Institutions don't form around non-categories.
Read it as a category forming *as an extension*, not a replacement.

🟡 **Probe-reported, could not verify — Gartner is behind bot protection:** a
2026-06-24 Gartner release predicting *"By 2028, AI coding costs will overtake the
average developer's salary."* Notably, the remedy Gartner reportedly recommends is
a governed engineering operating model — **process and platform controls, not
buying a cost-governance tool.** Worth chasing through a Gartner login if this ever
becomes load-bearing.

**The number that would settle it doesn't exist publicly.** No source publishes AI
spend as a share of total managed spend. The only survey measuring whether AI has
its own budget line at all is n=206 and self-selected (41% net-new money, 34% no
clear budget). Also flagged as untraceable: a widely-repeated *"73% of orgs report
AI costs blew their budget"* — no URL, no methodology, no primary source.

---

### The cautionary tale — read this one twice

**Sourcegraph is the closest analog to Orrery that exists, and it did not convert
to the agent era.** Code search and code intelligence — a visibility layer over
many repos. Valued at **$2.625B in 2021**. Since then: no funding round in five
years, self-serve tiers **killed in July 2025**, and a retreat to **Enterprise
only, "Starting at $16K"** — ✅ verified on their pricing page today, no individual
tier remains. Its AI bet, Amp, was spun out into a separate company in Dec 2025.

Federal procurement tells the same story: across USAspending, Sourcegraph appears
**once**, on a **$0-value** placeholder purchase order.

Whatever else this research says, that trajectory is the one to keep in view.

### Testing, migration and the rest — where the money actually went

**Migration is a services business wearing software clothing.** AWS publishes
**$0.003 per line of code** for Q Code Transformation. The IRS pays **Deloitte
$383,773,457 for a single CADE 2 task order** — over **$700M** to Deloitte on that
program alone, plus ~$221M to Accenture. Five orders of magnitude apart with
nothing in between; every serious modernization vendor is quote-only.

**And the AI-native startups have won essentially none of it.** USAspending
returns **zero awards** for Mechanical Orchard ($74M raised) and **zero** for
Moderne ($45M raised). The GAO baseline is bleaker still: of 10 critical federal
legacy systems, **only 3 of 10 modernizations were complete after six years** —
with unlimited budget and the world's largest integrators engaged.

**The genuinely strong category nobody lists is agent sandboxes.** Modal raised
**$355M at $4.65B (May 2026)** on **>$300M annualized revenue**, with sandboxes
alone **>1/3 of revenue**. Fly.io reports agent-native customers at ~2/3 of
revenue among its largest accounts. Selling *infrastructure agents run on* is
working; selling *observation of agents* is not.

**One competitor footnote:** **Vibe Kanban — named in the multiplayer research as
an unnamed competitor — is the pivoted remains of bloop AI**, a YC COBOL→Java
migration startup. The category we'd be entering is partly staffed by refugees
from categories that didn't work.

---

## 03 · The pricing unit is the tell — and it's worse than "priced at the manager"

An earlier draft of this doc claimed the tell was Exceeds AI charging *$65 per
manager per month*. **That figure comes from one probe and was never verified** —
Exceeds AI is seed-stage with no public funding figure. Don't cite it.

The verified data says something sharper. Of fifteen vendors, **only five publish a
price at all**, and the ones that do price like this:

> **LinearB** — billable user = *"any user assigned to at least one team."*
> *"You can have an unlimited number of users with access to LinearB with no
> additional cost."* Minimum billable: **30 seats** (Essentials) / **50**
> (Enterprise). ✅ Verified on their pricing page.
>
> **Waydev** — *"per active contributor."* **Managers and execs explicitly
> excluded** from billing.

So the unit isn't the manager. **The unit is the developer being measured, and the
people doing the looking are free.** A twelve-person team pays for thirty seats.
The developer is the unit of cost; the manager is the unit of value. That is the
economics of the thing stated in a price list.

**And the enterprise tier won't publish at all** — DX, Jellyfish, Faros, Uplevel,
Harness SEI all gate pricing behind "contact sales." The vendors with public
per-seat rates are the mid-market ones; everyone chasing $50k+ ACVs hides it.

**The same pattern turned up in code security, independently.** GitHub bills
**$19/active committer/month** for Secret Protection and **$30** for Code Security
(✅ verified on their page). Snyk, Semgrep and Socket all use effectively the same
unit — someone who committed to a monitored private repo in the last 90 days.

**And that unit is pointed the wrong way into the AI era.** Agents increase code
volume without increasing committers; in some org designs they *reduce* them. A
whole category monetises human commit activity at exactly the moment human commit
activity stops being the thing that scales. It is the most plausible mechanical
explanation for Snyk going from 27% to 7% growth, and it is a structural problem
nobody in the category has solved.

**A fourth instance, and it's the sharpest.** Greptile moved in March 2026 from a
flat $30/seat to **$30/seat + $1 per review beyond 50** — which at agentic PR
volume works out to roughly **$339 per seat per month**. Warp, Zed and Amp all
moved to credits or tokens. Sourcegraph abandoned self-serve entirely. Four
categories, same conclusion: **assume metered, not seated.**

**Three vendors already broke the model, in three different categories:**

- **Keypup** (analytics) prices **per repository** — $99/mo for two connected repos,
  scaling to $8/unit, *"unlimited users & contributors."*
- **Aikido** (security) prices **flat per org** — $300/mo Basic, $600/mo Pro — while
  its competitors charge $25–50 per developer. It reached a $1B valuation doing so.

If a per-seat model was ever going to feel wrong for a tool like Orrery, those are
two existing proofs that another axis works — and the AI-era pressure on per-seat
pricing is the reason to expect more of it.

### Sorted by who signs the cheque

- **Org / manager buys:** analytics, spend governance, security, review bots at
  team scale — paid for per developer surveilled
- **Developer buys:** the harness subscription — and at ~$800M/yr for Cursor
  alone, they buy it seriously
- **Developer loves, nobody buys:** read-your-own-transcripts (3,850★), AI-code
  tracking in git (2,477★), worktree cleanup, session viewers — all free, all
  monetizing at approximately zero

---

## 04 · What is demonstrably *not* being paid for

All four established in the multiplayer run, with receipts:

- **Cross-person agent analytics** — the working self-hosted implementation has
  **28 stars**
- **Session sharing and handoff** — ~30 projects, two with traction; the
  git-transport version got 15★/1 fork
- **Compliance and code provenance** — **CodeSlick built exactly this thesis and
  shut down in June 2026**: *"the paying customers weren't there"*
- **Agent-to-agent context handoff** — no accepted standard, nobody monetizing the
  payload

---

## 05 · What this means for Orrery

**The good news.** Developers paying $20–200/month out of pocket for a coding
agent is a real, large, proven behaviour. This is not a market where individuals
refuse to spend.

**The hard news.** That spend goes to the harness, and the harness vendors own it.
Everything adjacent that carries money has an org as the buyer — which is exactly
the side of the line Orrery deliberately doesn't stand on. Principle #1 (local,
no accounts, no telemetry, read-only, on the developer's side) is a credibility
asset and a revenue problem in the same sentence.

That tension is now confirmed from three independent directions: the Aug-10 team
research, the multiplayer probes, and the pricing units above. It is not a gap to
close — it's a property of the position, and the position is still the right one
for a free tool. **Just don't expect the free tool to become a business by adding
features.** If revenue ever matters, it will require choosing a different buyer,
and that is a `PRODUCT.md` decision, not a roadmap item.

**One live consolidation signal worth watching:** Cursor is now inside SpaceX and
Graphite is inside Cursor. The independent middle of this market is being bought.
Cross-vendor neutrality — Orrery's one structural edge — gets *more* valuable as
the vendors consolidate, and simultaneously harder to maintain as their formats
churn under new owners.

---

## 06 · Confidence and gaps

**Verified by hand:** the SpaceX–Cursor close and price; Cursor's revenue and
enterprise/individual split; Anthropic's Series G and both Claude Code figures.

**Probe-reported, not independently checked:** Copilot's user and revenue figures,
Cognition's numbers, the Cursor valuation ladder, all §02 categories.

**All categories completed**, including testing/QA and migration.

**The gap that actually matters — nobody knows who pays.** Stack Overflow 2025
(n≈49k), JetBrains DevEcosystem 2025 (n≈23k) and DORA 2025 (n≈5k) *all* measure AI
adoption and *none* asks whether the employer or the developer pays. The
individual-vs-company split does not exist in published research. The closest
proxy is Ramp's corporate-card data (70k+ US businesses — 43.5% pay Anthropic,
39.7% OpenAI as of July 2026), which is **100% employer-paid by construction** and
so can't answer the question either.

**Independent adoption signal, original data.** A hand-parse of 2,569 job posts
across eight HN "Who is hiring?" threads found tool-naming in JDs rose from ~1.3%
(May 2025) to ~8% (mid-2026), with **Claude Code overtaking Cursor from May 2026**.
Notably: **CodeRabbit, Jellyfish, LinearB, Braintrust and DX drew 0–2 mentions
between them across all 2,569 posts.** Employers name the harness in job specs.
They never name the measurement layer.

**Unresolved conflict:** the reported Snyk "$7.4B → $3.7B markdown" is not
corroborated at Sacra. Treat the ~$326M/7% figures as a Sacra estimate and the
markdown as unverified.

**Aggregator databases are leads, not evidence.** Tracxn's Greptile record shows a
$41.4M Series A at a $6.6M valuation — internally impossible. Getlatka, Growjo and
Tracxn revenue figures are algorithmic estimates throughout.

**Retracted from an earlier draft of this file:** the "Exceeds AI $65 per manager
per month" datapoint. Single-probe, unverified, and the verified pricing data
(§03) makes a stronger version of the same point without it.

**Source contamination warning.** This topic is unusually polluted. A whole tier of
sites — getpanto, serpsculpt, orbilontech, taskade, blog.exceeds.ai, codepulsehq,
pandev-metrics, codelitics and similar — publish precise-looking figures that
contradict vendors' own pages (e.g. a Faros "$29/contributor tier" and an
open-source Community Edition, neither of which exists on faros.ai). Getlatka,
Growjo and Tracxn revenue numbers are algorithmic estimates, not disclosures.
**Anything not traced to a filing, a funding announcement, a named publication, or
the vendor's own page should be assumed wrong.**

**Standing caution:** every ARR figure in this space that isn't in a filing is
vendor-published and reads as positioning, not traction.
