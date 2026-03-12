Checkout Experiment & Growth Analytics
Project Overview

This project analyzes the impact of a new checkout experience (Variant B) introduced by an e-commerce company to reduce checkout drop-offs and improve revenue. The goal is to build an end-to-end analytics solution that cleans raw data, constructs a reliable analytics layer, analyzes funnel performance, evaluates the A/B experiment, and delivers actionable business insights.

The project includes:

A Python-based ETL pipeline for data cleaning and transformation

Curated analytical datasets

Funnel and KPI analysis

A/B experiment evaluation

Business impact estimation

An interactive analytics dashboard built in Microsoft Power BI Desktop

The final output provides a decision-ready recommendation on whether the new checkout variant should be rolled out to all users.

Business Objective

The company launched a new checkout design (Variant B) to improve purchase completion and reduce friction during checkout.

Key questions addressed:

Should Variant B be rolled out to all users?

Where are the largest funnel drop-offs?

Which user segments drive conversion and revenue performance?

What is the expected revenue impact of rolling out Variant B over the next 30 days?

Project Structure
Capstone_CheckoutAnalytics/

README.md

data/
fact_sessions.csv
fact_orders.csv
dim_users_enriched.csv

etl/
etl_pipeline.py

analysis/
analysis.ipynb

dashboard/
dashboard.pbix
dashboard_screenshots/

final_story/
final_deck.pdf
Data Pipeline (ETL)

The ETL pipeline processes raw datasets and produces curated analytical tables.

Steps performed:

Load raw datasets

users.csv

sessions.csv

events.csv

orders.csv

order_items.csv

products.json

campaigns.csv

Data cleaning

Remove duplicate sessions

Handle missing values in device and channel fields

Normalize inconsistent text casing

Detect and cap extreme revenue outliers

Feature engineering

Funnel stage flags

Session duration and time-to-step metrics

Revenue metrics

Basket summaries

User-level aggregated metrics

Generated Datasets
fact_sessions.csv

Session-level dataset containing:

session_id

user_id

device

channel

campaign_id

experiment variant

funnel step flags

time-to-step metrics

session revenue fields

fact_orders.csv

Order-level dataset containing:

order_id

session_id

user_id

payment_method

net_amount

basket statistics

product category information

margin proxy

dim_users_enriched.csv

User-level dataset containing:

signup_date

user segment

city tier

preferred device

lifetime sessions

lifetime orders

repeat user flag

user value band

Analysis

The analysis notebook performs the following:

KPI Calculations

Core business metrics:

Conversion Rate

Revenue

Average Order Value

Revenue per session

Funnel stage conversions

Funnel Analysis

Reconstructs the user journey:

Product View → Add to Cart → Begin Checkout → Payment Attempt → Purchase

Identifies the largest drop-off points and potential friction areas.

A/B Experiment Analysis

Comparison between Variant A and Variant B:

Variant A conversion rate: 8.38%
Variant B conversion rate: 9.99%

Result:

Variant B delivers a ~19% relative improvement in conversion rate.

Segment Analysis

Performance evaluated across:

device

marketing channel

new vs returning users

product categories

Impact Estimation

Estimated impact of rolling out Variant B across all sessions:

projected increase in completed orders

projected incremental revenue over the next 30 days

Dashboard

An interactive analytics dashboard was created using Power BI.

The dashboard contains four main pages:

Executive Overview

Revenue

Orders

Average Order Value

Conversion Rate

Revenue trend

Funnel Analysis

Funnel step conversions

Drop-off analysis

Time-to-step insights

Segment Explorer

Performance comparison across:

device

channel

new vs returning users

product categories

Experiment Deep Dive

Variant A vs Variant B conversion comparison

segment-level experiment results

experiment insights

Dashboard screenshots are included in the dashboard_screenshots folder.

How to Run the ETL Pipeline

Install required Python packages

pip install pandas numpy

Navigate to the ETL directory

cd etl

Run the pipeline

python etl_pipeline.py

The script generates the curated datasets in the data directory.

Final Deliverables

This project includes:

Python ETL pipeline

Curated analytics datasets

Analysis notebook

Interactive Power BI dashboard

Final presentation summarizing insights and recommendations

Key Recommendation

The A/B experiment results show that Variant B significantly improves checkout conversion rates.

Based on the analysis, rolling out Variant B to all users is recommended, with further experimentation focused on reducing checkout friction and improving mobile purchase experiences.