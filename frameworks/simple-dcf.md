---
name: simple-dcf
id: 20260908T111736Z
tier: framework
domain: value-investing
author: Neo
tags: [dcf, valuation, cash-flow, scenarios]
links:
  - "data/DCF - Simple Clean.xlsx"
---

# Simple DCF - Fixed 10% Discount Rate

Run the same ten-year calculation for **base, bull and bear**. Keep the discount rate at **10% in every year and case**. Use the top-left model in `data/DCF - Simple Clean.xlsx` as the layout reference.

## 1. Receive the inputs

Metric selection and adjustments are decided separately. This framework only calculates the supplied inputs:

- `V0`: adjusted starting annual value.
- `g1`: annual growth for years 1-5.
- `g2`: annual growth for years 6-10.
- `X`: terminal multiple applied to the year-10 value.
- `A`: supplied adjustment from modeled value to common-equity value; use its supplied sign.
- `S`: diluted shares outstanding.

Record the company, valuation date and input sources. Use matching units for values and shares. Do not choose or redefine the metric here.

## 2. Set the cases

- **Base:** central, expected assumptions.
- **Bull:** favorable but plausible assumptions.
- **Bear:** adverse but plausible assumptions.[3]

Assign g1, g2 and X to each case. Keep V0, A and S consistent unless an explicit case adjustment is supplied. Do not change the discount rate.

## 3. Calculate each case separately

Here t is the forecast year, from 1 to 10; PV means present value; ^ means exponentiation.[1]

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

The final intrinsic value includes **both** the discounted annual values and the discounted terminal value. Terminal value is discounted for ten years, not eleven; do not add it twice.[1][2]

## 4. Check

**PASS:** all three cases calculated; 10% throughout; matching units; S > 0; terminal value and A applied once; bear <= base <= bull. Otherwise **HALT** and correct the input or calculation. Never invent a missing input or treat bear value as a guaranteed floor.

## Research basis

Compared with the workbook's `Standard Models!B1:F23`, brain DCF/terminal-value research and workspace `knowledge/simple-dcf-buffett-school.md`. This procedure uses the requested fixed 10%, not the workbook's stored 15%. Input selection must preserve the valuation basis.[4]

## Sources

[1] https://corporatefinanceinstitute.com/resources/valuation/dcf-formula-guide
[2] https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-terminal-value-formula
[3] https://corporatefinanceinstitute.com/resources/financial-modeling/scenario-analysis
[4] https://pages.stern.nyu.edu/~adamodar/pdfiles/acf3E/ch12.pdf

## Finished output

Fill every cell with that case's inputs and calculated results. The final column is its completed DCF value, including terminal value.

| Case | Growth 1-5 | Growth 6-10 | Terminal multiple | PV years 1-10 | PV terminal | Final intrinsic value/share |
|:--|--:|--:|--:|--:|--:|--:|
| Base | | | | | | |
| Bull | | | | | | |
| Bear | | | | | | |
