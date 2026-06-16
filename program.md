goal: improve sales-investigator skill so it finds best-fit real estate variants from requirements, upgrades the economic prediction formula, backtests predictions against historical actuals, and provides a current-market overview.
target_metric: eval_score out of 100
comparison_rule: higher is better; protected sections must remain unchanged; tie goes to clearer and shorter skill text
evaluation_command: rtk python3 tools/evaluate_sales_investigator.py skills/sales-investigator/SKILL.md
result_extraction: read target_metric/status/score_breakdown from evaluator output
max_iterations: 50
minimum_iterations: 30
per_iteration_timeout: 30 seconds
can_modify: skills/sales-investigator/SKILL.md, program.md, results.tsv, tools/evaluate_sales_investigator.py
cannot_modify: Core Behavior, Investigation Process, Real Estate Segmentation, Legal and Transaction Risk Screening sections inside skills/sales-investigator/SKILL.md
constraints: preserve core behavior, investigation process, real estate segmentation, and legal/transaction risk screening; do not weaken market evidence, outlier filtering, forecasting scenarios, or completion criteria.
