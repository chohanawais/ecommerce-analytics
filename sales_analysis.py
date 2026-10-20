import pandas as pd

df = pd.read_csv("data/sales.csv")


df["revenue"] = df["quantity"] * df["unit_price"]
df["total_cost"] = df["quantity"] * df["cost_price"]
df["profit"] = df["revenue"] - df["total_cost"]


print("=" * 40)
print("E-COMMERCE SALES ANALYSIS")
print("=" * 40)

print("TOtal Order:", len(df))
print("Total Revenue: Rs.", df["revenue"].sum())
print("Total cost: Rs.", df["total_cost"].sum())    
print("Total Profit: Rs.", df["profit"].sum())


print("\nProduct Sales:")
print(df.groupby("product")["quantity"].sum())

print("\nProfit by Product:")
print(df.groupby("product")["profit"].sum())


