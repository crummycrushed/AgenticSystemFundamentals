import numpy as np

a = np.array([1, 2,3])

print(a + 10)


# Why ??
# Numpy treat 10 like:
# [10, 10, 10]
# And adds


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])
print(matrix.shape)
print(vector.shape)
print(matrix + vector)


# [[10, 20, 30]
# [10, 20, 30]]



mat = np.array([[1, 2], [3, 4]])
vec = np.array([2, 3])
print(vec + mat)