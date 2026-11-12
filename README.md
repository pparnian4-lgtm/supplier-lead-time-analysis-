# Supplier Lead Time Analysis

Python analysis of supplier lead times and delivery risk, with an automated summary report. All data is synthetic.

## About the data
- 600 purchase orders from 20 suppliers (2024-2025)
- Generated with `generate_data.py` (fixed random seed, so results are reproducible)
- Columns: supplier, country, material, quantity, promised days, actual days, defect rate, waste

## Questions this project answers
- Which suppliers are the most late or the most unpredictable?
- Is delay related to defect rate or material waste?
- Which countries perform best?

## How to run
pip install pandas matplotlib
python generate_data.py

## Project structure
- `generate_data.py`: creates the synthetic dataset
- `data/orders.csv`: the generated orders

## Findings
Coming soon.
