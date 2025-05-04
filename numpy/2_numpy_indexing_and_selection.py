import numpy as np

# Creating a sample array
arr = np.arange(0, 11)
print("Initial array:", arr)

# Bracket indexing and selection
# Get a value at an index
print("Value at index 8:", arr[8])

# Get values in a range
print("Values in range [1:5]:", arr[1:5])
print("Values in range [0:5]:", arr[0:5])

# Broadcasting
# Setting values with index range
arr[0:5] = 100
print("After broadcasting [0:5] with 100:", arr)

# Reset array
arr = np.arange(0, 11)
print("Reset array:", arr)

# Important notes on slices
slice_of_arr = arr[0:6]
print("Slice of array [0:6]:", slice_of_arr)

# Change slice
slice_of_arr[:] = 99
print("After modifying slice:", slice_of_arr)
print("Original array after modifying slice:", arr)

# To get a copy
arr_copy = arr.copy()
print("Copy of array:", arr_copy)

# 2D arrays
arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
print("2D array:\n", arr_2d)

# Indexing row
print("Second row of 2D array:", arr_2d[1])

# Getting individual element value
print("Element at [1,0]:", arr_2d[1][0])
print("Element at [1,0] (alternative syntax):", arr_2d[1, 0])

# 2D array slicing
print("Shape (2,2) from top right corner:\n", arr_2d[:2, 1:])
print("Bottom row:", arr_2d[2])
print("Bottom row (alternative syntax):", arr_2d[2, :])

# Conditional selection
arr = np.arange(1, 11)
print("Array for conditional selection:", arr)

# Check condition
print("Condition arr > 4:", arr > 4)

# Store boolean results in another array
bool_arr = arr > 4
print("Boolean array for arr > 4:", bool_arr)

# Select elements where condition is True
print("Elements where arr > 4:", arr[bool_arr])

# Using condition directly in selection
print("Elements where arr > 2:", arr[arr > 2])

# Using a variable for condition
x = 2
print("Elements where arr > x (x=2):", arr[arr > x])
