import numpy as np

a = np.array([10,20,30])
print(a.shape)

#meaning
# 3 numbers in 1 straight line

# Real life example:
# 3 exam score
# 3 temperatures
# 3 prices


# 2D Array (Matrix)

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(b.shape)

# 2 rows and 3 columns
# real life example
# excel sheet
# studen table
# dataset (rows and colums)


# threee or more dimensions
# Numpy supports arbitratily many dimensions

c = np.zeros((10, 28, 28))
print(c.shape)
#print(c)
# meaning 
# 10 item
# each values has 28 rows
# each row has 24 colums


# what does np.zeros()  ^
# created an array 
# with shape (2,3)
#Fill it with 0


# Why use it ?
# when we want to create emtpy dats

# 5 studens , 3 subjects
#print(np.zeros((5,3)))



# What does np.ones() mean ?
z = np.ones((5, 3))
print(z)


# What is a shape ?
# Shape tells:
# how many rows
# How many columns
# how many layers


# arr_name[row][col]
z[0][1] = 12
print(z)



