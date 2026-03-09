mport pandas as pd # noqa: F401


df = pd.read_csv("sales_data.csv")




# clear names reduce confusion.


df = df.rename(columns={"Price": "UnitPrice", "Discount": "DiscountPercent"})
print(df)






#Drop


df_2 = df.drop(columns=["OrderDate", "DiscountPercent"])
print(df_2)
