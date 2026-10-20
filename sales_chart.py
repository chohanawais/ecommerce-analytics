import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/ecommerce.db")

query = """
SELECT
     product,
     SUM(revenue) AS total_revenue,
     SUM(profit) AS total_profit
FROM sales
GROUP BY product
ORDER BY total_revenue DESC 
LIMIT 10
"""


df = pd.read_sql_query(query, conn)
conn.close()


print(df.to_string(index=False))


df.plot(
        x="product",
        y=["total_revenue", "total_profit"],
        kind="bar",
        figsize=(10, 6)
        )


plt.title("Top 10 Products: Sales and Profit")
plt.xlabel("Product")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/sales_profit_chart.png")

print("Chart saved to data/sales_profit_chart.png")
