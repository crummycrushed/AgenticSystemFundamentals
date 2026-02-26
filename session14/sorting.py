import pandas as pd


# Sorting by 1 column
df = pd.read_csv("employees.csv")

x = df.sort_values("Salary", ascending=False)

#print(x)



# Sorting by mulitple columns

z = df.sort_values(["Salary", "PerformanceScore"], ascending=[True, False])
#print(z)


x = df.sort_index(ascending=False)
print(x)

