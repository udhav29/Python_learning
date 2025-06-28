import numpy as np
print("-----program 1-----")
random_array = np.random.rand(4, 2)
empty_array = np.empty((4, 2))
zeros_array = np.zeros((3, 5))
ones_array = np.ones((4, 3, 2))

print("Random Array (4x2):\n", random_array)
print("\nEmpty Array (4x2):\n", empty_array)
print("\nZeros Array (3x5):\n", zeros_array)
print("\nOnes Array (4x3x2):\n", ones_array)


print("\n\n\n-----program 2-----")
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)


print("\n\n\n-----program 3-----")
vector = np.zeros(10)
vector[5] = 11
print(vector)


print("\n\n\n-----program 4-----")
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)


print("\n\n\n-----program 5-----")
arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)
print(float_arr)
print(float_arr.dtype)
