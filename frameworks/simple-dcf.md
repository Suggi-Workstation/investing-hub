---
name: simple-dcf
id: 20260908T111736Z
tier: framework
domain: value-investing
author: Neo
tags: [dcf, valuation, cash-flow, scenarios]
---

# Simple DCF - Fixed 10% Discount Rate

## 1. Fix the basis

Record company, valuation date, currency, units, selected metric, historical period and whether the supplied amounts belong to the business or common shareholders. Review 5-10 years of the supplied metric, including a weak period; identify changes that make the starting year unrepresentative.

Keep the discount rate at **10% in every year and case**, including sensitivity checks. Treat it as the fixed required-return convention, not a measured company-specific cost of capital. Use annual amounts and year-end discounting throughout.

Receive metric selection, normalization and cash-conversion adjustments as inputs; do not decide them here. If supplied earnings have not been reconciled to distributable cash after required reinvestment, label the result **discounted-earnings proxy**, not a cash-flow valuation. Growth MUST NOT assume that the same money is both distributed and reinvested.

## 2. Assemble the inputs

| Input | Required entry |
|:--|:--|
| V0 | Supplied normalized starting annual amount; positive for this simple growth model. |
| g1 | Annual growth for years 1-5, entered as a decimal greater than -1. |
| g2 | Annual growth for years 6-10, entered as a decimal greater than -1. |
| X | Non-negative exit multiple of the same year-10 metric. |
| A | Supplied, signed adjustment from modeled value to common equity, as of the valuation date. |
| S | Positive point-in-time diluted share count, in units matching V0 and A. |
| P | Share price and timestamp, only if comparing value with price. |

Attach a filing period or assumption label to each input in the working calculation. Itemize A; count cash, debt, leases, preferred claims and non-operating assets only as the supplied valuation basis requires. Do not automatically subtract debt from an equity-basis model. Reconcile share classes and potential dilution; do not substitute time-weighted earnings-per-share denominators without checking them.

## 3. Set Base, Bull and Bear

Assign g1, g2 and X independently to each case:

- **Base:** a defensible central path from normalized performance, not management's target by default.
- **Bull:** better demand, execution or durability that can plausibly occur together; no stacked best-ever assumptions.
- **Bear:** a credible setback, competitive erosion or slower recovery; allow negative growth where justified.

Give each case one sentence explaining its growth and exit assumptions. Check growth against market size, competition and the supplied reinvestment requirement. Usually moderate growth in years 6-10; justify any acceleration. Choose X for a mature year-10 business, not automatically today's multiple or a historical peak.

Keep V0, A and S common unless a documented scenario-specific adjustment is supplied. Check subsequent financing, acquisitions and share issuance before calling the valuation current. Do not create a probability-weighted value to conceal downside.

## 4. Calculate each case

Here t is the forecast year, from 1 to 10; PV means present value; ^ means exponentiation.

```text
Years 1-5:  V_t = V0 * (1 + g1)^t
Years 6-10: V_t = V0 * (1 + g1)^5 * (1 + g2)^(t - 5)

PV of year t    = V_t / 1.10^t
PV of years 1-10 = SUM(PV of each of the ten years)
Terminal value  = V_10 * X
PV of terminal  = Terminal value / 1.10^10

Equity value = PV of years 1-10 + PV of terminal + A
Final intrinsic value/share = MAX(0, Equity value) / S
```

Calculate with full precision; round only displayed results. Keep the unrounded equity value visible if it is negative, even though the displayed common-share value is floored at zero.

For each positive intrinsic value: `30% MoS price = value/share * 0.70`; `50% MoS price = value/share * 0.50`. If P is supplied, `actual margin of safety = 1 - P / value/share`. Mark this ratio N/A when value/share is zero. These are price cushions, not trade instructions.

## 5. Challenge and verify

- Recalculate Base with g1 and g2 both zero, holding X, A and S fixed. Treat this as a no-growth sensitivity, not liquidation value or a guaranteed floor.
- Reduce Base X and growth separately; record which change moves value most. Keep 10% fixed. Flag when the conclusion depends mainly on a generous exit multiple.
- Calculate terminal dependence as `PV terminal / (PV years 1-10 + PV terminal)`; do not include A in that denominator or force a target percentage.
- Before release, MUST verify finite inputs, basis, units, financing date, all ten annual discounts, year-10 terminal discount, and single application of A. Verify `Bear <= Base <= Bull`; investigate reversed ordering rather than relabeling rows. A second calculation MUST reproduce the results.

**PASS:** the checks reconcile and material uncertainties are disclosed. **HALT:** missing inputs, unsupported conversion to cash, inconsistent claims or unreconciled calculations prevent the stated valuation. Report a proxy explicitly where applicable. Bear is a scenario, never a downside floor.

## Finished output

Give one input line: company/date, metric and basis, V0, A, S, optional P. Give one short confidence line: High / Medium / Low, key sensitivity and what would change the estimate. Use exactly these three result rows; include both forecast and terminal value in the completed intrinsic value. No essay.

| Case | g1 / g2 / X | PV years 1-10 | PV terminal | Intrinsic value/share | 30% MoS price | 50% MoS price |
|:--|:--|--:|--:|--:|--:|--:|
| Base | | | | | | |
| Bull | | | | | | |
| Bear | | | | | | |
