import pandas as pd # noqa: F401


df = pd.read_csv("sales_data.csv")




df["Revenue"] = df["Quantity"] * df["Price"]


print(df)
# What is the total revenue per region


df_rev = df.groupby("Region")["Revenue"].sum()
print(df_rev)




# Whic region earns most ?
df_rev_sort = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print(df_rev_sort)




# What is the average revenue per reigion
df_avg_rev = df.groupby("Region")["Revenue"].mean()
print(df_avg_rev)