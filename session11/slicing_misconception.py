import numpy as np

a = np.array([10, 20, 999, 40])
b = a[1:3]

#b = [20, 999]
#b[1] = 30 --> 999
print(b)
b[1] = 999

print(b)

print(a)

# Why did original change ?

# Because slicing creates a view
# view means
# same memory
# just looking at the part of it
# This behavious is intentional for performance but require awareness


d = np.array([1, 2, 3, 4])
e = d[1:3].copy()
e[0] = 999
print(d)
print(e)