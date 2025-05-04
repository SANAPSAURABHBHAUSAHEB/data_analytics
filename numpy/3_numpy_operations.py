import numpy as np

# Creating a sample array
arr = np.arange(0, 10)
print("Array:", arr)

# Basic arithmetic
print("Addition (arr + arr):", arr + arr)
print("Multiplication (arr * arr):", arr * arr)
print("Subtraction (arr - arr):", arr - arr)

# Division (handling division by zero)
print("Division (arr / arr):", arr / arr)  # Warning: division by zero (0/0 = nan)

# Division by array with zero at first position
print("Reciprocal (1 / arr):", 1 / arr)  # Warning: division by zero (1/0 = inf)

# Exponentiation
print("Cube (arr ** 3):", arr ** 3)

# Universal functions
print("Square root of arr:", np.sqrt(arr))
print("Exponential (e^arr):", np.exp(arr))
print("Sine of arr:", np.sin(arr))
print("Natural log of arr:", np.log(arr))  # Warning: log(0) = -inf

# Summary statistics
print("Sum of elements:", arr.sum())
print("Mean of elements:", arr.mean())
print("Maximum value:", arr.max())
print("Minimum value:", arr.min())
print("Variance:", arr.var())
print("Standard deviation:", arr.std())

# 2D arrays
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\n2D Array:\n", arr_2d)

# Column-wise sum
print("Column-wise sum (axis=0):", arr_2d.sum(axis=0))

# Shape of the 2D array
print("Shape of 2D array:", arr_2d.shape)

# Row-wise sum
print("Row-wise sum (axis=1):", arr_2d.sum(axis=1))

# Reversing an array
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print("Reversed Array:", reversed_arr)

# Sorting an array
arr = np.array([5, 2, 8, 1, 3])
sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

# Maximum in an array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Index of Maximum Value in 2D Array:", np.argmax(arr_2d))
print("Index of Maximum Value along rows:", np.argmax(arr_2d, axis=1))  # Max value along each row
print("Index of Maximum Value along columns:", np.argmax(arr_2d, axis=0))  # Max value along each column



