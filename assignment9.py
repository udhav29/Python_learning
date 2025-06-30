import numpy as np

print("\n\n\n\n\n-----program 1-----")
arr1d = np.array([1, 2, 3])
arr2d = np.array([[4, 5, 6]])
combined = np.vstack((arr1d, arr2d))
print("Combined (vstack):\n", combined)
combined_h = np.hstack((arr1d.reshape(-1, 1), arr2d.T))
print("Combined (hstack):\n", combined_h)

print("\n\n\n\n\n-----program 2-----")
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
flattened = arr2d.flatten()
print("Flattened array:", flattened)

print("\n\n\n\n\n-----program 3-----")
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)
print("\n\n\n\n\n-----program 4-----")
# Get Max and Min Values
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Max:", np.max(arr))
print("Min:", np.min(arr))
# Get Shape (rows & columns)
rows, cols = arr.shape
print("Rows:", rows, "Cols:", cols)
for row in arr:
    for item in row:
        print(item, end=' ')
print()

# Specific element (e.g. row 1, col 2)
print("Element at [1][2]:", arr[1][2])


# Sum of 2D Array Using for Loop
total = 0
for row in arr:
    for item in row:
        total += item
print("Sum:", total)



#Arithmetic Operations Between Arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Addition
print("Add:\n", a + b)

# Subtraction
print("Subtract:\n", a - b)

# Multiplication (element-wise)
print("Multiply:\n", a * b)

# Division (element-wise)
print("Divide:\n", a / b)

