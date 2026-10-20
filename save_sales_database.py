import pandas as pd
import sqlite3


df = pd.read_csv("data/sales.csv")


df["revenue"] = df["quantity"] * df["unit_price"]
df["total_cost"] = df["quantity"] * df["cost_price"]
df["profit"] = df["revenue"] - df["total_cost"]

conn = sqlite3.connect("data/ecommerce.db")

df.to_sql("sales", conn, if_exists= "replace", index=False)


print("Sales data saved to SQLite database!")
print("Total records:", pd.read_sql_query(
    "SELECT COUNT(*) AS total FROM sales", conn
    ).iloc[0, 0])


conn.close()
