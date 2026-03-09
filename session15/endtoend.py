import pandas as pd


df = pd.read_csv("sales_data.csv")






#fill
df["Discount"] = df["Discount"].fillna(0)
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Price"] = df["Price"].fillna(df["Price"].median())




df["Revenue"] = df["Quantity"] * df["Price"]


df = df.rename(columns={"Price": "UnitPrice"})


df = df.drop(columns=["OrderDate"])


summary = df.groupby("Region").agg({
   "Revenue": ["sum", "mean"],
   "OrderID": ["count"]
})


print(summary)