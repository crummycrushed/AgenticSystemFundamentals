import pandas as pd # noqa: F401


df = pd.read_csv("sales_data.csv")




# detect missing data


#print(df.isnull())




# Count missing values per column:


#print(df.isnull().sum())








#Avengers  IronMan  Hulk
#Avengers  ""     ""   --> remove ?




# Drop missing value


df_clean = df.dropna()
print(df)
#print(df_clean)




# Drop only rows where Quantity is missing
df_clean2 = df.dropna(subset=["Quantity", "Price"])
#print(df_clean2)






# drop columns with missing value


df_clean3 = df.dropna(axis=1)
#print(df_clean3)






#strategy 2 : Fill missing value
# instead of removing data , replace missing with logical value


# Fill discount 0
df["Discount"] = df["Discount"].fillna(0)


print(df)




median = df["Price"].median()
df["Price"] = df["Price"].fillna(median)
print(df)
