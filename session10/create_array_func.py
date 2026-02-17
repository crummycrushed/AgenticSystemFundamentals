# from existing data

import numpy as np
np.array([1, 2, 3])


# Create a numpy array with empty values  0s
empty_arr = np.zeros(5)
print(empty_arr)


# create a numpy array with value as 1 for 10 elements
one_arr = np.ones(10)
print(one_arr)

print(type(one_arr))


# create evenly spaces values (like range)
arange_numpy = np.arange(0, 20, 2)
print(arange_numpy)



# evenly spaced values
# linspace : lineraly spaced numbers --> it generates evenly sapced numbers between a start and end value

linear_np = np.linspace(0.01, 1.01, 5)
print(linear_np)
# means:
# start = 0
# stop = 1
# total number = 5
# include both 0 and 1

# step  = (stop - start ) / (num - 1) = (1 - 0) / (5 - 1) = 1/4 = 0.25
# step          value
#. 0            0
#. 1            0.25
#. 2            0.5
#  3            0.75
#  4            1