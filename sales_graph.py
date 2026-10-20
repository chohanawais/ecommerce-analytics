import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv")


df["order_date"] = pd.to_datetime(df["order_date"])
df["revenue"] = df["quantity"] * df["unit_price"]
df["cost"] = df["quantity"] * df["cost_price"]
df["profit"] = df["revenue"] - df["cost"]
df["month"] = df["order_date"].dt.strftime("%Y-%m")


monthly = df.groupby("month")[["revenue", "profit"]].sum()

monthly.plot(kind="bar", figsize=(10, 6))


plt.title("Monthly Salesw and Profit")
plt.xlabel("Month")
plt.ylabel("Amount (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("reports/monthly_sales_profit.png")
print("Graph saved successfully!")

