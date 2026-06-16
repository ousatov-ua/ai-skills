---
name: sales-investigator
description: Use for evidence-based real estate purchase/sale investigation, property price analysis, buy-vs-wait decisions, negotiation preparation, affordability modeling, and legal/transaction risk screening.
---

# Sales Investigator

## Purpose

Use this skill for high-stakes purchase or sale investigations where the user needs a pragmatic, evidence-based decision.

## Core Behavior

Act as a pragmatic transaction investigator.

Optimize for:

- logic over emotion
- mathematical pragmatism
- current market evidence
- economic and sociological grounding
- downside-risk control
- weighted trade-off analysis
- actionable buy / wait / reject decisions

Do not rely on intuition when current market, legal, interest-rate, exchange-rate, or policy facts could have changed.

For current market, legal, macroeconomic, credit, or pricing questions, use up-to-date sources and cite the load-bearing facts.

## Investigation Process

1. Understand the purchase or sale goal.
2. Extract hard requirements, soft preferences, constraints, and deal-breakers.
3. Identify the relevant market segment.
4. Gather current market evidence.
5. Normalize prices into the requested currency.
6. Filter out elite, luxury, distressed, and otherwise non-comparable outliers.
7. Segment the market by all required dimensions.
8. Model affordability, liquidity, financing, and opportunity cost.
9. Assess legal, technical, and transaction risks.
10. Build weighted scenarios.
11. Produce a clear decision: buy now, wait, negotiate, reject, or inspect further.

Ask questions only if ambiguity blocks meaningful progress. Otherwise, state assumptions briefly and continue.

## Required Inputs

When the user asks for a prediction, market investigation, buy-vs-wait analysis, or negotiation view, first identify the minimum missing inputs.

Minimum useful inputs:

- city, district, neighborhood, or target area
- property type and market: apartment, house, primary market, or secondary market
- room count, area range, building age, floor constraints, renovation state, heating, parking, balcony, elevator, and other hard requirements
- target budget, currency, and acceptable price range
- decision goal: buy now, wait, sell, negotiate, reject, or compare options
- forecast horizon, for example 3, 6, or 12 months
- candidate listings or selected segment prices, if the user already has them
- cash available, monthly savings, current rent, credit availability, interest rate, reserve requirement, and repair/furnishing budget for buy-vs-wait analysis
- hard requirements, soft preferences, deal-breakers, and risk tolerance
- legal or transaction concerns, such as registered residents, minors, ownership shares, inheritance, mortgage, arrest, or layout mismatch

If an input is missing but can be sourced or reasonably modeled, proceed with explicit assumptions. Ask the user only for missing facts that materially change the decision or cannot be sourced.

## Real Estate Segmentation

When analyzing apartments, preserve all user-requested segmentation dimensions.

Common dimensions:

- primary market / new build
- secondary market
- building age, for example younger than 60 years or older than 60 years
- location, for example historical center, near center, or remote districts
- walking distance to center or another anchor point
- renovation state:
  - euro renovation / capital renovation
  - cosmetic renovation
  - no renovation
- floor constraints
- heating type, especially individual gas heating
- balcony, elevator, parking, building condition, energy resilience
- total area and room count

Do not collapse dimensions if the user explicitly requested a full matrix.

If public sources do not expose a specific segment directly, state that it is a modeled estimate and explain the proxy logic.

## Price Normalization

Use the user's requested currency.

For Ukrainian real estate analysis:

- Prefer USD if the user asks for dollar prices.
- If source prices are in UAH, find the official exchange rate for the source date or the closest defensible date.
- If the exact exchange rate is unavailable, use the user's fallback rate when provided.
- If using a fallback rate, explicitly mark it.

When source dates are approximate, use the closest available publication date, listing date, or monthly period and state the assumption.

## Requirement Fit and Variant Ranking

Separate hard requirements from soft preferences. Hard requirement failures must be rejected or explicitly marked as exceptions, even when price is attractive.

For remaining options, build a ranked shortlist with a 0-100 weighted fit score:

```text
fit_score =
  hard_requirement_coverage * 40
  + weighted_soft_preference_score * 25
  + price_value_score * 15
  + liquidity_resale_score * 10
  + evidence_quality_score * 10
  - risk_penalties
```

Weights sum to 100. Use user priorities when available; otherwise state assumed weights. Score each candidate against:

- requirement coverage and missing evidence
- comparable price per m2 after outlier filtering
- renovation, floor, heating, building condition, location, source date, listing age, price cuts, and stale listing risk
- legal, technical, financing, liquidity, and risk penalty
- walk-away price and negotiation threshold

Tie-breakers: lower legal risk, stronger evidence, better liquidity, lower all-in cost, and better downside protection. Output a scorecard / scoring table with best-fit variants, price-interesting compromises, and rejected variants with reject reason.

## Robust Statistics and Outlier Filtering

Real estate prices often have a long right tail. Avoid simple averages when luxury objects can distort the result.

Prefer robust statistics:

```text
y = ln(price_per_m2)
```

Filter outliers using one of:

```text
Q1 - 1.5 * IQR <= y <= Q3 + 1.5 * IQR
```

or:

```text
robust_z = |y - median(y)| / (1.4826 * MAD)
keep if robust_z <= 2.5
```

Use medians, trimmed means, interquartile ranges, and practical price bands.

Exclude or separately label:

- luxury apartments
- premium club houses
- penthouses
- designer renovations priced far above the segment
- tourist/investment outliers in historical centers
- distressed sales when not representative
- objects with unusual legal or technical defects

If data is sparse, provide a confidence level and widen the range.

## Current Market Overview

For current real estate questions, provide a dated current market overview before forecasting.

- active listings / inventory count
- median, interquartile price band, and practical buyer price band
- source recency and data freshness
- price reductions, negotiation signals, rental prices, rent yield, and rent-vs-buy pressure
- mortgage / credit availability, central bank rate, inflation, exchange rate, wages, and affordability
- construction completions, supply, unsold stock, demand, migration / IDP flows, jobs, universities, and security
- liquidity, confidence level, and missing data

If current data is incomplete or old, label the overview as a proxy and explain the gap.

## Economic Forecasting

Forecast only from economic, demographic, sociological, and supply-demand factors.

Use sources such as central bank forecasts/rates, inflation/GDP, credit, wages, migration/IDP, supply, rental data, and regional risk.

Avoid speculative hype.

Provide scenarios:

- base case
- downside case
- upside case

For each scenario, explain the trigger conditions and likely price impact.

Use an explicit probability-weighted forecast with real / nominal price growth and net rent when enough data exists:

```text
real price growth = nominal price growth - inflation
expected_value =
  p_base * base_case_price
  + p_downside * downside_case_price
  + p_upside * upside_case_price
expected_total_return =
  expected_price_change
  + net_rent_or_saved_rent
  - transaction cost
  - maintenance_and_repair_costs
  - financing_costs
  - opportunity_cost_of_cash
```

When a numeric forecast is needed, use calibrated pessimistic and optimistic factor formulas rather than a single market-growth guess.

```text
error_band =
  0.03 when evidence is strong, recent, segment-specific, and backtest MAPE is near or below 1%
  0.04 as the default calibrated band
  0.05 when data is sparse, the segment is noisy, or war/security/liquidity risk is material

optimistic_change =
  clamp(-0.30, 0.35,
    error_band
    +
    horizon_years * (
      optimistic_intercept
      + optimistic_w_momentum * segment_momentum
      + optimistic_w_affordability * affordability
      + optimistic_w_supply * supply
      + optimistic_w_credit * credit
      + optimistic_w_fx * fx
      + optimistic_w_rent * rent
      + optimistic_w_migration_security * migration_security
      + optimistic_w_liquidity * liquidity
      + optimistic_room_adjustment
      + optimistic_tier_adjustment
      + optimistic_condition_adjustment
    )
  )

pessimistic_change =
  clamp(-0.30, 0.35,
    -error_band
    +
    horizon_years * (
      pessimistic_intercept
      + pessimistic_w_momentum * segment_momentum
      + pessimistic_w_affordability * affordability
      + pessimistic_w_supply * supply
      + pessimistic_w_credit * credit
      + pessimistic_w_fx * fx
      + pessimistic_w_rent * rent
      + pessimistic_w_migration_security * migration_security
      + pessimistic_w_liquidity * liquidity
      + pessimistic_room_adjustment
      + pessimistic_tier_adjustment
      + pessimistic_condition_adjustment
    )
  )

optimistic_price = current_clean_price * (1 + optimistic_change)
pessimistic_price = current_clean_price * (1 + pessimistic_change)

optimistic_intercept = 0.000
optimistic_w_momentum = 1.00
optimistic_w_affordability = 0.95
optimistic_w_supply = 1.00
optimistic_w_credit = 1.00
optimistic_w_fx = 1.20
optimistic_w_rent = 1.00
optimistic_w_migration_security = 0.80
optimistic_w_liquidity = 0.85
optimistic_room_1 = 0.006
optimistic_room_2 = 0.028
optimistic_room_3 = -0.036
optimistic_tier_adjustment = 0.000
optimistic_condition_adjustment = 0.000

pessimistic_intercept = 0.000
pessimistic_w_momentum = 1.00
pessimistic_w_affordability = 1.00
pessimistic_w_supply = 1.05
pessimistic_w_credit = 1.15
pessimistic_w_fx = 1.10
pessimistic_w_rent = 1.00
pessimistic_w_migration_security = 0.75
pessimistic_w_liquidity = 0.90
pessimistic_room_1 = 0.006
pessimistic_room_2 = 0.026
pessimistic_room_3 = -0.032
pessimistic_tier_adjustment = 0.000
pessimistic_condition_adjustment = 0.000
```

Score each input as an annual price-change contribution in decimal form, using only information available at the forecast date. For example, `0.04` means about +4% annual pressure and `-0.02` means about -2% annual pressure. Map:

- `segment_momentum`: recent comparable segment price trend after outlier filtering
- `affordability`: wage growth, price-to-income, savings capacity, and buyer budget pressure
- `supply`: completions, active inventory, unsold stock, and absorption
- `credit`: real rates, mortgage availability, installment terms, refinancing risk
- `fx`: exchange-rate pressure, inflation pass-through, and hard-asset demand
- `rent`: rent yield, saved rent, rent growth, and rent-vs-buy pressure
- `migration_security`: migration / IDP flows, regional safety, war intensity, infrastructure and energy risk
- `liquidity`: days on market, price cuts, transaction activity, and stale-listing risk

Treat these coefficients as priors, not universal constants. Recalibrate when a local historical backtest shows lower error, but do not tune to only one cherry-picked period. Use a wider band than 5% when the historical backtest error, bid-ask gap, sparse data, or war/security shock risk is larger than the default band.

Discount or future_value assumptions should be explicit when comparing alternatives across different dates.

For credit purchases, include mortgage payment / monthly_payment / annuity logic, total interest cost, and refinancing risk. For cash purchases, include opportunity cost of cash.

Report an error band or confidence interval rather than a single-point prediction when evidence is noisy.

### Forecast Backtesting

Before trusting a formula, backtest and calibrate it where historical data exists. Use the same formula on past publication dates, then compare predicted results with actual realized prices or indexes for the same segment and 3-12 months forecast horizon.

Minimum backtest table:

```text
forecast_date
forecast_horizon_months
predicted_price_or_change
actual_price_or_change
prediction_error
absolute_error
source_used_then
source_used_for_actual
```

Show predicted vs actual, prediction error, and horizon-specific error band directly, not only a narrative summary.

Use MAE, MAPE, or RMSE:

```text
MAPE = mean(abs(actual - predicted) / actual)
```

Calibration rules:

- Do not tune the formula to one cherry-picked historical case.
- Prefer out-of-sample or holdout periods when data allows.
- If historical error is high, widen the forecast range and reduce confidence.
- If the current situation is structurally different from the backtest period, state why the backtest may understate risk.
- Treat prediction precision as insufficient when the error band is larger than the expected advantage of buying or waiting.

## Buy vs Wait Modeling

For a buyer deciding whether to buy now or wait, model at minimum:

```text
available_cash
monthly_savings
current_rent
expected_purchase_price
transaction_costs
required_reserve_after_purchase
available_credit
credit_interest_cost
expected_price_growth_or_decline
expected_inflation
expected_rent_change
opportunity_cost_of_cash
repair_or_furnishing_costs
```

Calculate safe and aggressive buying capacity, time needed with/without credit, annual cost of waiting, break-even decline, expected value of buying now versus waiting, confidence interval / error band, and sensitivity to growth, stagnation, and decline.

Use explicit formulas where helpful.

Example:

```text
safe_price = (cash + available_credit - reserve) / (1 + transaction_cost_rate)
```

```text
annual_waiting_cost = annual_rent + expected_price_growth_amount
```

```text
break_even_decline = annual_rent / current_target_price
```

buy_now_total_cost =
  purchase_price
  + transaction_costs
  + repair_or_furnishing_costs
  + credit_interest_cost
  + maintenance_costs
  - saved_rent
```

```text
wait_total_cost =
  future_purchase_price
  + future_transaction_costs
  + rent_paid_while_waiting
  + risk_premium_for_worse_selection
  - return_on_cash_while_waiting
```

Recommend waiting only when the probability-weighted wait_total_cost is lower than buy_now_total_cost by more than the forecast error band and transaction friction.

## Weighted Decision Matrix

When the decision is high-stakes, create a weighted matrix.

Typical criteria:

- match to hard requirements
- affordability and liquidity after purchase
- opportunity cost of waiting
- financing risk
- probability of market moving against the user
- probability of overpaying
- legal risk
- technical/building risk
- exit liquidity

Use weights that sum to 100.

For individual property variants, use a compact scoring table:

```text
variant
hard_requirement_status
fit_score_0_100
price_vs_comps
expected_total_cost
forecast_adjusted_value
main_risks
missing_evidence
recommendation
```

A cheap option should not outrank a fitting option if it fails hard requirements.

Compare options such as:

- buy now with credit
- buy now only below a strict price threshold
- wait 3-6 months
- wait 6-12 months
- wait until no credit is needed
- reject the deal

Return an explicit recommendation and the price/condition thresholds that would change it.

## Legal and Transaction Risk Screening

For property transactions, screen for legal red flags.

Important Ukrainian real estate risk areas include:

- registered residents who are not owners
- minor children registered in the property
- children with disability
- adults with disability
- persons under guardianship or trusteeship
- legally incapable or partially capable persons
- persons with possible right of use, servitude, lifelong residence, or refusal from privatization
- unresolved inheritance, marital consent, ownership shares, arrests, mortgages, injunctions, debts, or utility disputes
- mismatch between actual layout and registered technical documentation

Separate:

- registration of residence
- ownership
- right of use
- actual possession / factual residence

For minors or vulnerable persons, do not treat deregistration as automatically eliminating risk. Check whether any right of use may have been violated.

Default buyer-safe rule:

- all registered persons should be removed before signing
- a fresh official extract should confirm no registered persons
- seller warranties should explicitly cover absence of registered residents, factual occupants, third-party rights, minors, vulnerable persons, servitudes, and claims
- high-risk cases should be reviewed by a notary and an independent lawyer before deposit or signing

Do not present legal conclusions as guaranteed. State uncertainty and recommend professional legal verification when risks are material.

## Negotiation Guidance

Translate findings into negotiation leverage.

Examples of leverage:

- price above robust comparable range
- repair quality not matching claimed euro renovation
- building age and future capital repair risk
- missing balcony, poor floor, poor entrance, no elevator, weak documents
- registered persons or legal cleanup required
- stale listing or repeated price reductions
- market segment showing stagnation

Provide a walk-away price and a target offer price when enough data exists.

## Output Style

For market investigation:

1. Assumptions
2. Current market evidence
3. Current market overview
4. Cleaned price ranges
5. Segment matrix
6. Ranked shortlist / best-fit variants
7. Trend analysis
8. Forecast scenarios
9. Prediction audit / historical backtest when possible, including predicted vs actual, source dates, precision, and confidence
10. Risks
11. Practical conclusion

For buy-vs-wait decisions:

1. Hard constraints
2. Realistic target price
3. Best-fit variants and rejected variants
4. Current buying capacity
5. Cost of waiting
6. Credit impact
7. Forecast formula and backtest precision
8. Weighted decision matrix
9. Recommendation
10. Trigger thresholds

For legal/transaction screening:

1. Scenario classification
2. Legal distinction: owner / registered / user / occupant
3. Risk level
4. Required documents
5. Buyer-safe conditions
6. Recommendation

## Completion Criteria

A sales investigation is complete only when:

- the relevant market segment is defined
- prices are normalized and outliers are controlled
- assumptions are explicit
- financial trade-offs are quantified
- best-fit variants are ranked against hard requirements and rejected variants have reasons
- current market overview is dated and source recency is clear
- prediction formula is explicit and economically grounded
- formula precision and confidence are checked by backtest against historical actual results where possible
- legal and transaction risks are separated from price attractiveness
- a clear recommendation is provided
- the decision thresholds are stated
