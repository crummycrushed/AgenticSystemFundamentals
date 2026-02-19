import numpy as np
            # 0.  1.  2.  3.  4
a = np.array([10, 10, 30, 40, 50])

# [20 30 40]

print(a[1:4])



# 2D slicing

matrix = np.array([
  [1, 2, 3],  
  [4, 5, 6],
  [7, 8, 9]
])

# [[2 3]
#.  [5 6]]

# first 2 rows --> 0:2
# column 1 and 2 : 1:3


#.   0. 1. 2
# 0 [1, 2, 3],  
# 1 [4, 5, 6], # 1. , 0, 1, 2
# 2 [7, 8, 9]. # 2, 0, 1, 2

print(matrix[1:3, 0:3])




