# Checkout Experiment & Growth Analytics

An end-to-end e-commerce analytics project covering ETL, A/B experiment evaluation, funnel analysis, and a Power BI dashboard — with a final recommendation on whether to roll out a new checkout experience.

---

## Business Objective

An e-commerce company launched a redesigned checkout flow (Variant B) to reduce drop-offs and increase purchase completion. This project answers:

- Should Variant B be rolled out to all users?
- Where are the largest funnel drop-offs?
- Which user segments drive the most conversion and revenue?
- What is the projected revenue impact of a full rollout over 30 days?

---

## Key Finding

| Metric | Variant A | Variant B |
|---|---|---|
| Conversion Rate | 8.38% | 9.99% |
| Relative Lift | — | **+19.2%** |

**Recommendation: Roll out Variant B.** Results are statistically significant. The largest remaining opportunity is reducing mobile checkout friction.

---

## Project Structure

```
Checkout-Experiment-And-Growth-Analytics/
│
├── Raw/                        # Source datasets (users, sessions, events, orders, products, campaigns)
├── ETL/
│   └── etl_pipeline.py         # Data cleaning, feature engineering, output table generation
├── Processed/                  # Curated analytical tables (fact_orders, fact_sessions, dim_users)
├── Analysis/
│   └── analysis.ipynb          # KPIs, funnel analysis, A/B test, segment breakdown, impact estimate
├── Dashboard/
│   ├── Ecommerce_Analytics_Dashboard.pbix
│   └── Dashboard_Screenshots/
└── Final_story/
    └── final_memo.pdf          # Decision-ready summary memo
```

---

## Dataset

Synthetic dataset of 2,200 users, 9,036 sessions, 18,945 events, and 707 orders across 220 products. Raw data includes intentional quality issues (missing values, duplicate sessions, inconsistent casing) to simulate a real pipeline.

Source files: `users.csv`, `sessions.csv`, `events.csv`, `orders.csv`, `order_items.csv`, `products.json`, `campaigns.csv`

---

## ETL Pipeline

```bash
pip install pandas numpy
cd ETL
python etl_pipeline.py
```

Produces three output tables in `Processed/`:

- **fact_orders** — order-level metrics: basket size, top category, margin proxy, avg rating
- **fact_sessions** — session-level metrics: funnel stage flags, event count, conversion flag, campaign info
- **dim_users** — user-level aggregates: lifetime value, total orders, avg order value

---

## Analysis

The notebook (`Analysis/analysis.ipynb`) covers:

- **Funnel reconstruction** — Product View → Add to Cart → Begin Checkout → Payment Attempt → Purchase
- **A/B experiment evaluation** — conversion rate comparison with statistical significance testing
- **Segment analysis** — by device, channel, and new vs. returning users
- **30-day revenue impact estimate** — projected incremental orders and revenue from full rollout

---

## Dashboard

Built in Power BI Desktop. Four pages:

1. **Executive Overview** — revenue, AOV, conversion rate, revenue trend
2. **Funnel Analysis** — step-by-step drop-off rates and time-to-step
3. **Segment Explorer** — performance by device, channel, user type, product category
4. **Experiment Deep Dive** — Variant A vs B across all segments

Screenshots in `Dashboard/Dashboard_Screenshots/`.

---

## Tools

Python · pandas · Power BI · Jupyter
