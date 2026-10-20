import pandas as pd 
import sqlite3


conn = sqlite3.connect("data/ecommerce.db")

query = """
SELECT
     product,
     SUM(quantity) AS total_sold,
     SUM(revenue) AS total_revenue,
     SUM(profit) AS total_profit
FROM sales
GROUP BY product
ORDER BY total_sold DESC
LIMIT 5
"""


df = pd.read_sql_query(query, conn)


print("=" * 60)
print("TOP 5 BEST-SELLING PRODUCTS")
print("=" * 60)
print(df.to_string(index=False))
print("=" * 60)

conn.close()

