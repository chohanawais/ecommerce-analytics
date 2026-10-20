import pandas as pd

df = pd.read_csv("data/sales.csv")

df["order_date"] = pd.to_datetime(df["order_date"])
df["revenue"] = df["quantity"] * df["unit_price"]
df["cost"] = df["quantity"] * df["cost_price"]
df["profit"] = df["revenue"] -df["cost"]


df["month"] = df["order_date"].dt.strftime("%Y-%m")


monthly = df.groupby("month").agg(
        total_orders=("order_id", "count"),
        total_sales=("revenue", "sum"),
        total_profit=("profit", "sum")
        )


print("MONTHLY SALES REPORT")
print("=" * 50)
print(monthly)

