# The Recon Advisor

A chatbot in the Streamlit UI that explains what a run did and recommends
configuration changes. It is **evidence-first**: every statement it makes is
derived from data the platform already stored — run metrics, per-field
comparison results, exception samples and column profiles. It does not
speculate and it does not invent numbers.

It works with no external service. An optional LLM adds narrative phrasing on
top of the same findings.

---

## 1. Where to find it

* **Advisor page** — pick a reconciliation and a run, chat about it.
* **Run detail** — findings for that run inline.
* **Designer** — "Suggest matching logic" builds a draft rule set from
  profiled columns, which you can accept into the builder.

API: `POST /api/advisor/chat`, `POST /api/advisor/analyse`,
`GET /api/advisor/profiles`, `POST /api/advisor/suggest-match-logic`.

---

## 2. What it reads

`ReconAdvisor.build_context()` assembles an evidence bundle:

| Evidence | Source |
|---|---|
| Run outcome, timings, totals | `reconciliation_run` |
| Per-leg counts | `reconciliation_leg_run` |
| Per-field compared/matched/mismatched | `reconciliation_field_metrics` |
| Exception sample (bounded) | `reconciliation_exceptions` |
| Exception counts by type and field | Aggregated in the metrics DB |
| Recent run history (10) | `reconciliation_run` |
| The definition itself | MongoDB |
| Column profiles | `column_profiles` in MongoDB, written when a run is asked to profile its sources |

If a piece is unavailable, the advisor says what it could not see rather than
guessing. Missing evidence is a stated limitation of an answer, never a gap
filled by assumption.

---

## 3. What it can tell you

### Why records did not match

The distinction that matters operationally: **a key that does not line up**
versus **a feed that is genuinely incomplete**.

The advisor compares one-sided counts on both sides. Roughly symmetric
`LEFT_ONLY` and `RIGHT_ONLY` populations mean the rows are probably present on
both sides but the key is not aligning them — a key problem. A large
one-sided imbalance means data is actually missing — a feed problem. It says
which, and why it concluded that.

### Which columns to match on

From column profiles it ranks shared columns by:

* **uniqueness** — a key must be selective
* **null density** — a NULL-heavy column makes a poor key component
* **measured cross-source value overlap** — how many distinct values actually
  appear on both sides, computed rather than assumed
* **normalisation gain** — the same overlap re-measured after trim, case
  folding and leading-zero stripping. If normalising raises overlap
  materially, it recommends the normalisation with the key.

It also proposes a composite key when no single column is selective enough,
and hands back a ready-to-paste `keys:` fragment.

### Which comparison rule fits

`classify_difference()` looks at the actual expected/actual pairs in the
exception sample and labels each one:

| Classification | Recommendation |
|---|---|
| `case_only` | `case_insensitive` |
| `whitespace_only` | `trimmed`, or a `trim` normalisation |
| `leading_zeros` | `stripLeadingZeros` on the key or field |
| `numeric_small` | `numeric_tolerance` with a tolerance derived from the observed spread |
| `numeric_large` | Not a tolerance problem — investigate the feed |
| `date_format` | `dateFormat` / `parseDateFormats` normalisation |
| `date_offset` | `date_tolerance`, with the observed offset (often a timezone) |
| `truncation` | Field-length difference upstream |
| `one_side_missing` | Coverage, not comparison |
| `unrelated` | Genuinely different values — a real break |

Tolerances are rounded to a sane business value rather than the raw maximum
observed, and the advisor shows the distribution it derived them from.

### Whether your matching logic is pulling its weight

Because each rule's outcome is materialised per row and aggregated, the
advisor can say:

* a rule that **never matched** — dead configuration, or a column that is
  never populated
* a rule that **always matched** — contributing nothing under `AND`,
  short-circuiting everything under `OR`
* an `OR` where one rule carries essentially all the matches

### Duplicates, data quality, performance, scheduling

Duplicate key concentrations and what they imply about grain; null and
distinct-count anomalies against previous runs; skew and shuffle observations
from run timings; and whether a run repeatedly waits for data at the same
time of day, which is usually a schedule that fires before the feed lands.

---

## 4. How a question is answered

1. `detect_intent()` routes the question by keyword to one of:
   `key_selection`, `matching_logic`, `unmatched`, `tolerance`, `duplicates`,
   `exceptions`, `performance`, `data_quality`, `schedule`, `summary`,
   `help`, or `general`.
2. The relevant deterministic analysis runs over the evidence bundle
   (`advise_from_run()`, `advise_from_profile()`, `suggest_match_logic()`).
3. Findings are ranked by severity (`CRITICAL`, `WARNING`, `SUGGESTION`,
   `INFO`) and category (`KEY_SELECTION`, `MATCHING_RULE`, `NORMALIZATION`,
   `TOLERANCE`, `DATA_QUALITY`, `DUPLICATES`, `COVERAGE`, `PERFORMANCE`,
   `OPERATIONS`).
4. Each finding carries **the evidence behind it** and, where applicable, a
   configuration fragment you can paste into the designer.
5. If LLM enrichment is on, the same findings are handed to the model as
   structured evidence with an instruction to phrase, not to invent. The
   deterministic findings are still displayed. If the call fails or times
   out, the answer degrades silently to the deterministic text.

---

## 5. Optional LLM enrichment

| Variable | Default |
|---|---|
| `ADVISOR_LLM_ENABLED` | `false` |
| `ANTHROPIC_API_KEY` | unset (required when enabled) |
| `ADVISOR_LLM_MODEL` | `claude-sonnet-5` |
| `ADVISOR_LLM_MAX_TOKENS` | `1200` |
| `ADVISOR_LLM_TIMEOUT` | `45` |

### Privacy

**Leave it off unless sending run metadata off-site is approved.** When
enabled, the request carries the evidence bundle: column *names*, counts,
metric values, and **sample expected/actual values from exceptions** — which
are business data. Credentials and connection configuration are never
included, but the exception samples are real values.

The deterministic advisor is complete without it. Enrichment changes the
prose, not the conclusions.

---

## 6. Profiling

Column profiles are what make key recommendation quantitative rather than
heuristic. Ask for them when running:

```bash
curl -X POST /api/reconciliations/{id}/run -d '{"profileSources": true}'
```

or tick **Profile sources** on a manual run in the UI. Profiling adds a pass
over each source to compute per-column null counts, distinct counts, sample
values and cross-source overlap, so it costs time — it is opt-in, and it is
worth doing once when onboarding a feed and again when a feed changes shape.

Without profiles the advisor still works from run metrics and exceptions; it
just cannot rank *unused* columns as key candidates, and it says so.

---

## 7. What it will not do

* It will not change your configuration. Every recommendation is a fragment
  you review and apply; there is no auto-apply path.
* It will not report a number it did not read from stored evidence.
* It will not tell you a break is acceptable. Classifying a difference as
  `numeric_small` is a statement about the data, not a decision to tolerate
  it — that decision, and its comment, belongs to the officer.
