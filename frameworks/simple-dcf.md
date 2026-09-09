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

Keep the discount rate at **10% in every year and case**, including sensitivities. Use nominal cash/earnings and growth in the stated valuation currency. Treat 10% as the required-return convention, not measured financing cost or a guarantee that enterprise and equity approaches give the same value. Year 1 is the next twelve months from the valuation date; rebase fiscal-period inputs accordingly. Discount each annual amount at period-end and terminal value immediately after the year-10 distribution.

Receive metric selection, normalization and cash-conversion adjustments as inputs; do not decide them here. Growth MUST NOT count the same money as both distributed and reinvested. Check that the supplied cash conversion remains consistent with forecast investment, not just the starting year.

Use this model only when a positive two-stage path represents the annual benefits. Known zero/negative years, expiry before year 10, abrupt shutdowns or uneven funding needs require a dated cash-flow schedule or another method. Do not normalize these events away; X = 0 does not remove post-expiry forecast cash.

## 2. Assemble the inputs

| Input | Required entry |
|:--|:--|
| V0 | Positive, supplied normalized annual run-rate at the valuation date; a total amount, not a per-share amount. |
| g1 | Annual growth for years 1-5, entered as a decimal greater than -1. |
| g2 | Annual growth for years 6-10, entered as a decimal greater than -1. |
| X | Non-negative exit multiple of the same year-10 metric. |
| A | Supplied signed total adjustment to common equity at the valuation date; same currency and scale as V0. |
| S | Positive current common share count, or explicitly reconciled diluted-equivalent count. Match the numerical scale: monetary millions with shares in millions. |
| P | Share price and timestamp, only if comparing value with price. |

Attach a filing/date/page or assumption label to every input. Convert per-share inputs to totals before calculation. Itemize A; include cash, debt, leases, preferred/minority claims and non-operating assets only as the supplied basis requires. Do not automatically subtract debt from an equity-basis model.

Use one method for existing noncommon equity claims: deduct their supplied economic value in A and use basic common shares; or use a justified diluted-equivalent S with exercise proceeds and A reconciled. Never apply both to the same claim. Separate existing awards from future compensation already charged in the forecast; do not charge the same future grants again through dilution or replacement buybacks. Check share classes, vesting and expense timing; an earnings-per-share weighted-average denominator is not automatically today's S.

## 3. Set Base, Bull and Bear

Assign g1, g2 and X independently to each case:

- **Base:** a defensible central path from normalized performance, not management's target by default.
- **Bull:** better demand, execution or durability that can plausibly occur together; no stacked best-ever assumptions.
- **Bear:** a credible setback, competitive erosion or slower recovery; allow negative growth where justified.

Give each case one sentence explaining growth and X. Check market size, competition and supplied reinvestment; justify acceleration in years 6-10. Support X with continuing cash conversion, reinvestment, growth and durability. Identify fundamental versus market-derived X; do not automatically copy today's multiple or a historical peak.

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
Modeled value/share = MAX(0, Equity value) / S
```

Calculate with full precision; round only displayed results. Keep the unrounded equity value visible if it is negative, even though the displayed common-share value is floored at zero.

For a positive modeled value: `price at 30% discount = value/share * 0.70`; `price at 50% discount = value/share * 0.50`. If P is supplied, `discount to modeled value = 1 - P / value/share`; mark it N/A at zero value. Apply the valuation-type labels below; these comparisons are not trade instructions.

## 5. Challenge and verify

- Recalculate Base with g1 and g2 both zero, holding X, A and S fixed. Treat this as a no-growth sensitivity, not liquidation value or a guaranteed floor.
- Reduce Base X and growth separately over plausible ranges; record each input change and its value effect before naming the dominant sensitivity. Keep 10% fixed. Flag dependence on generous exit assumptions.
- If X represents a perpetuity of the same distributable cash with no payout change, check implied continuing growth: `gT = (0.10 * X - 1) / (X + 1)`. Assess its plausibility; do not apply this identity to earnings, EBITDA or finite-life assets. Zero growth in years 1-10 does not establish zero growth afterward.
- Calculate terminal dependence as `PV terminal / (PV years 1-10 + PV terminal)`; do not include A in that denominator or force a target percentage.
- Before release, MUST verify finite inputs, basis, units, financing date, all ten annual discounts, year-10 terminal discount, and single application of A. Verify `Bear <= Base <= Bull`; investigate reversed ordering rather than relabeling rows. A second calculation MUST reproduce the results.

**PASS:** applicable cash/claim identities and arithmetic reconcile, assumptions are traceable and limitations reach the final labels. **HALT** missing inputs, inconsistent claims, an unrepresentable path or unsupported valuation claims. Unsupported cash conversion blocks a cash-DCF claim, not an explicitly labeled earnings proxy. Bear is a scenario, never a downside floor.

## Finished output

Give one input line: company/date, currency, metric/claimholder basis, V0, A, S, optional P and valuation type. Select the type in this order:

- **Earnings proxy:** earnings not reconciled to distributable cash; disclose any market-derived X too.
- **Market-multiple hybrid:** cash reconciled, but X is market-derived.
- **Cash DCF:** cash reconciled and terminal assumptions supported by fundamentals. Only this type may call value/share **intrinsic value** and the discounts **margin of safety**.

Give one confidence line: High / Medium / Low, decisive uncertainty, sensitivity and reassessment trigger. Confidence cannot exceed support for the weakest conclusion-critical assumption; repeated versions of one claim are not independent evidence. If case types differ, identify the type in each value cell. Keep proxy/hybrid labels; do not rename their markdowns MoS. Use exactly these three rows for a completed calculation; otherwise return Not calculable / Not applicable and the blocker, with values N/A.

| Case | g1 / g2 / X | PV years 1-10 | PV terminal | Value/share (type above) | Price at 30% discount | Price at 50% discount |
|:--|:--|--:|--:|--:|--:|--:|
| Base | | | | | | |
| Bull | | | | | | |
| Bear | | | | | | |
