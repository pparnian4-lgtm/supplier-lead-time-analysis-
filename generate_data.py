"""Generate a synthetic supplier order dataset.

All data is made up. It does not come from any real company.
Run:  python generate_data.py
Output: data/orders.csv
"""
import csv
import os
import random
from datetime import date, timedelta

random.seed(42)

COUNTRIES = ["Germany", "Turkey", "China", "India", "Italy", "Poland", "Finland", "Spain"]
MATERIALS = ["Cast steel", "Stainless steel", "Aluminium alloy", "Bearings", "Fasteners", "Machined parts"]

# 20 suppliers, each with its own typical behaviour (so the analysis has something to find)
suppliers = []
for i in range(1, 21):
    suppliers.append({
        "supplier_id": f"S{i:02d}",
        "supplier_name": f"Supplier {i:02d}",
        "country": random.choice(COUNTRIES),
        "promised_days": random.choice([14, 21, 28, 35, 42]),
        "avg_delay": random.uniform(-2, 9),      # typical delay in days
        "delay_spread": random.uniform(1, 7),    # how unpredictable they are
        "defect_base": random.uniform(0.3, 4.0), # % defective
        "waste_base": random.uniform(1.0, 8.0),  # % material waste
    })

start = date(2024, 1, 1)
rows = []
order_id = 1
for _ in range(600):
    s = random.choice(suppliers)
    order_date = start + timedelta(days=random.randint(0, 729))
    delay = round(random.gauss(s["avg_delay"], s["delay_spread"]))
    actual = max(5, s["promised_days"] + delay)
    rows.append({
        "order_id": f"PO{order_id:04d}",
        "supplier_id": s["supplier_id"],
        "supplier_name": s["supplier_name"],
        "country": s["country"],
        "material": random.choice(MATERIALS),
        "order_date": order_date.isoformat(),
        "quantity": random.randint(50, 2000),
        "promised_days": s["promised_days"],
        "actual_days": actual,
        "defect_rate_pct": round(max(0, random.gauss(s["defect_base"], 0.8)), 2),
        "waste_pct": round(max(0, random.gauss(s["waste_base"], 1.2)), 2),
    })
    order_id += 1

rows.sort(key=lambda r: r["order_date"])

os.makedirs("data", exist_ok=True)
with open("data/orders.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} orders from {len(suppliers)} suppliers to data/orders.csv")
