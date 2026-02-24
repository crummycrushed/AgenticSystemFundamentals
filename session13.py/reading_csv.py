import pandas as pd

df = pd.read_csv("employee.csv")
#print(df)


# That single line:
# opens the file
# parese rows and columns
# data type infer
# constrcuted a dataframe


val = df.head(10)
#print(val)


#this helps to verify:
# column names
# data format
# basic structure 
# no of columns


val_2 = df.tail(10)
#print(val_2)


val_3 = df.iloc[2 : 7]
#print(val_3)




info = df.info()
#print(df.info())


#provides:
# number of rows
# columns names
# data types
# count of non null values


desc = df.describe()
print(desc)
