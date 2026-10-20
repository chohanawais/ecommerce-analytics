import pandas as pd
import sqlite3


conn = sqlite3.connect("data/ecommerce.db")

query= """
SELECT
     SUM(revenue) AS total_revenue,
     SUM(total_cost) AS total_cost,
     SUM(profit) AS total_profit,
     COUNT(*) AS total_records
FROM sales
"""


report = pd.read_sql_query(query, conn)


print("=" * 40)
print(" E-COMMERCE SALES REPORT")
print("=" * 40)


print("Total Records:", report["total_records"][0])
print("Total Revenue:", round(report["total_revenue"][0], 2))
print("Total Cost:", round(report["total_cost"][0],2))
print("Total Profit:", round(report["total_profit"][0], 2))

print("=" * 40)

conn.close()
