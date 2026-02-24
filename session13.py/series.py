import pandas as pd

arr = pd.Series([90, 85, 80])
print(arr)


arr_2 = pd.Series([90, 85, 80], index=["Alice", "Bob", "Charlie"])
print(arr_2)



# Suppose you are analyziung 
# Daily temperature

# how will u create a pandas sereies


temp = pd.Series([100, 200, 123, 23], index=["Mon", "Tue", "Wed", "Thu"])
print(temp)