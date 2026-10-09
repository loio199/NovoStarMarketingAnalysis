# NovoStar Marketing Analysis — Methodology

**Scope:** July 2024–June 2026 · **Currency:** EUR

This document explains **what was done, why, and how to reproduce it**. Business findings and recommendations are kept in the separate final write-up.

## How we approached the spending decision

The Head of Marketing asked whether campaign spending should continue. We treated this as a **value-for-money and causal-effect question**, not simply a request to rank campaigns by sales.

Our decision framework was:

1. **Establish the sales baseline:** Measure completed-order revenue over time so campaign results are considered in the context of the wider business.
2. **Start with marketing's reported view:** Calculate attributed revenue and revenue ROAS by campaign and channel. This shows what the available attribution system credits to marketing.
3. **Ask whether attributed sales cover costs:** Deduct estimated product costs, then compare the remaining contribution with each campaign's budget. Review returns and cancellations separately to avoid treating unsuccessful orders as realized revenue.
4. **Check what type of demand campaigns attract:** Distinguish first observed purchases from repeat purchases and compare customer behavior across acquisition channels. This helps frame acquisition-versus-retention trade-offs, without assuming new purchases are incremental or repeat purchases are not.
5. **Challenge the attribution story:** Compare weekly sales with the previous year and examine attributed versus unattributed revenue. These provide context, **not** a valid untreated control group.
6. **Turn uncertainty into a decision rule:** Model different hypothetical incremental shares of attributed contribution and calculate the share required to cover each campaign budget. Use the results to identify where spending requires stronger evidence rather than presenting scenarios as proven impact.

We deliberately **did not claim to calculate actual incremental return**. The data has no verified exposure history or randomized holdout, so it cannot show what customers would have done without a campaign. The final write-up uses this evidence to discuss which spending warrants review, cautious continuation, or further testing. For future decisions, we recommend a randomized holdout that compares **incremental completed-order contribution net of campaign cost**, with longer-term follow-up for acquisition campaigns.

## Approach and design choices

| Step | What we did | Why |
|---|---|---|
| **1. Audit** — `Notebooks/01_data_audit.ipynb` | Checked completeness, duplicates, key relationships, dates, statuses, campaign timing, and order/item totals. | Identify issues that could distort sales or campaign metrics before analysis. |
| **2. Clean** — `Notebooks/02_data_cleaning.ipynb` | Removed exact duplicate customer and order records; standardized country labels; flagged suspicious dates, negative amounts, pre-signup orders, and campaign-date exceptions. Preserved order-item rows and original financial amounts. | Make transformations transparent without guessing how to repair uncertain records. Raw CSVs remain unchanged. |
| **3. Analyze** — `Notebooks/03_marketing_performance.ipynb` | Evaluated completed-order trends, campaign/channel attribution, product contribution, returns, customer purchasing patterns, first-purchase order mix, weekly comparisons, and sensitivity scenarios. | Assess whether attributed sales cover estimated costs, examine customer mix, and distinguish descriptive performance from evidence of causal impact. |
| **4. Validate** — `Notebooks/04_validate_results.ipynb` | Used known-answer calculations, accounting consistency checks, transaction spot checks, comparisons with exported tables, and an alternative treatment of duplicated order-item rows. | Catch implementation mistakes and test whether important conclusions depend on uncertain data assumptions. |

## Key calculation rules

- **Reporting population:** July 2024–June 2026. Main revenue metrics use completed orders with non-negative recorded totals; returned and cancelled orders are counted separately for order-outcome rates.
- **Revenue ROAS:** campaign-attributed completed-order revenue ÷ recorded campaign budget.
- **Estimated product cost:** sum of `quantity × unit_cost_eur` across an order's items.
- **Estimated product contribution:** recorded completed-order total − estimated product cost.
- **Contribution ROAS:** campaign-attributed product contribution ÷ campaign budget.
- **Contribution after budget:** campaign-attributed product contribution − campaign budget.
- **First versus existing purchase:** based on the earliest reliably dated completed purchase observed for each customer; this is not a verified causal acquisition measure.
- **Incrementality sensitivity:** hypothetical incremental share × attributed product contribution − campaign budget. Break-even share is budget ÷ attributed product contribution, where positive. These scenarios are **not** estimates of actual marketing lift.

## Assumptions and limitations

- **Attribution is not causation.** A campaign ID indicates recorded attribution, not proof the purchase was caused by marketing. Orders without a campaign ID are **not** an untreated control group.
- **Budget is a spending proxy.** `budget_eur` is used because verified actual campaign spending is not available.
- **Contribution is not full profit.** Shipping, payment processing, support, overhead, and other costs are not fully captured. Product unit costs are treated as estimates for historical purchases.
- **Uncertain source records were not silently corrected.** Suspected placeholder order dates are excluded by the reporting-period rule; inconsistent order/item totals and repeated order-item rows remain documented limitations. Exact customer and order duplicates were removed after checking for conflicting IDs.
- **Customer comparisons are descriptive.** Acquisition channels and campaign attribution describe different concepts, and customers have unequal time to make repeat purchases.
- **Historical comparisons are contextual.** Year-over-year and active-versus-inactive campaign weeks do not control for seasonality, selection, or previous marketing exposure.

## Validation

The implemented checks passed when run in the local project environment. An alternative calculation excluding exact duplicate order-item rows was used as a **robustness scenario**, not as proof those rows were erroneous. Recorded order totals were preserved despite reconciliation exceptions. Passing tests supports computational consistency but cannot establish source-data accuracy or campaign incrementality.

## Tools and reproducibility

**Tools:** Python, pandas, NumPy, Matplotlib, Jupyter Notebook, and Git. Project dependencies are declared in `requirements.txt` and `pyproject.toml`.

Prerequisites:
- Anaconda or Miniconda installed
- Git installed (to clone the repository)

From the repository root:

```bash
conda create -n novostar python=3.11
conda activate novostar
pip install -e .
jupyter notebook
```

Select the project Python kernel and run the notebooks in order: **01 → 02 → 03 → 04**. Inputs are in `data/raw/`; cleaned datasets are saved to `data/processed/`; tables and figures are written to `outputs/`. Restart the kernel and run all cells to check reproducibility.

## AI usage disclosure

**ChatGPT (OpenAI)** was used to help structure the workflow, draft and review Python and Markdown, suggest validation checks, and clarify interpretation. **Claude (Anthropic)** was consulted for alternative analysis ideas, including contribution-based metrics, customer mix, and incrementality sensitivity. The analysis was executed locally on the supplied data, and I(the author) proposed and reviewed the methodology, wrote most of the code, checked outputs, and is responsible for the final submission.
