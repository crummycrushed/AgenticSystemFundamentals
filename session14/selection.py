import pandas as pd

df = pd.read_csv("employees.csv")

x = df["Salary"]

#print(x)


y = df[["Name", "Salary"]]
#print(y)


# select name, Department, PerformanceScore

z = df[["Name", "Department", "PerformanceScore"]]

print(z)

