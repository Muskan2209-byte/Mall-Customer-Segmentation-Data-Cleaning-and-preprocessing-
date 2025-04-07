# Mall Customer Segmentation Data - Cleaning Summary

## Objective
Clean and preprocess the raw dataset for analysis and modeling.

## Changes Made
- Removed 1 duplicate row.
- Standardized 'Gender' text values to lowercase (`male`, `female`).
- Renamed all column headers to lowercase with underscores:
  - `CustomerID` → `customerid`
  - `Annual Income (k$)` → `annual_income_k$`
  - `Spending Score (1-100)` → `spending_score_1_100`
- Verified and fixed column data types (`int` for numeric values).

## Tools Used
- Python (Pandas)

## Files
- `mall_customers_cleaned.csv`: Final cleaned dataset.
- `cleaning_script.py`: Code used for data cleaning.
- `README.md`: This summary.
