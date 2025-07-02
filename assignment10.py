import numpy as np
print("-----program1-----")
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr, nan=0)
arr[:, [0, 1, 2]] = arr[:, [2, 1, 0]]
print("Modified Array:\n", arr)


print("\n\n-----program2-----")
arr_3d = np.arange(2*3*4).reshape(2, 3, 4)
moved = np.moveaxis(arr_3d, 0, -1)
print("Moved Axes Array Shape:", moved.shape)


print("\n\n-----program3-----")
arr = np.array([[1, np.nan, 3], [4, 5, np.nan]])
col_mean = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_mean, inds[1])
print("NaN Replaced with Column Average:\n", arr)


print("\n\n-----program4-----")
arr = np.array([[-1, 2, -3], [4, -5, 6]])
arr[arr < 0] = 0
print("Negative Replaced with 0:\n", arr)


print("\n\n-----program5-----")
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:\n", avg)


print("\n\n-----program6-----")
from scipy import stats
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
combined = np.concatenate((arr1, arr2), axis=0)
print("Mean:", np.mean(combined))
print("Median:", np.median(combined))
print("Mode:", stats.mode(combined, axis=None, keepdims=False).mode)


print("\n\n-----program7-----")
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
B = np.array([9, -6, 17])
X = np.linalg.inv(A).dot(B)
print("Solution (x, y, z):", X)


print("\n\n-----program8-----")
import matplotlib.pyplot as plt
semesters = ["Sem 1", "Sem 2"]
marks = [78, 85]
plt.plot(semesters, marks, marker='o', color='purple', linestyle='--', label='Marks')
plt.title("Semester Results Comparison")
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()
plt.show()



