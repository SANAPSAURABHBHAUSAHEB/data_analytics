import numpy as np

# Basic arrays
arr1 = np.array([1, 2, 3, 4])  # 1D array from a list
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array from a nested list
arr3 = np.array((7, 8, 9))  # 1D array from a tuple
print("Basic Arrays:\n", arr1, "\n", arr2, "\n", arr3)

# Special arrays
zeros = np.zeros((2, 3))  # 2x3 array of zeros
ones = np.ones((3, 2))  # 3x2 array of ones
identity = np.eye(3)  # 3x3 identity matrix
print("\nSpecial Arrays:\nZeros:\n", zeros, "\nOnes:\n", ones)

empty = np.empty((2, 2))  # 2x2 uninitialized array
full = np.full((2, 2), 7)  # 2x2 array filled with 7
print("\nEmpty:\n", empty, "\nFull:\n", full, "\nIdentity:\n", identity)

# Creating arrays with range
range_arr = np.arange(0, 10, 2)  # 1D array from 0 to 10 with step 2
linspace_arr = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
print("\nRange and Linspace Arrays:\n", range_arr, "\n", linspace_arr)

# Random arrays
rand = np.random.rand(2, 3)  # Random values in [0, 1), 2x3 shape
random_numbers = np.random.uniform(1, 100, 10)
rand_int = np.random.randint(1, 10, (2, 2))  # Random integers in [1, 10]
rand_normal = np.random.randn(2, 3)  # Random numbers from standard normal distribution
rand_custom_normal = np.random.normal(5, 2, (2, 3))  # Normal distribution with mean=5, std=2
print("\nRandom Arrays:\n", rand, "\n", rand_int, "\nStandard Normal:\n", rand_normal, "\nCustom Normal:\n", rand_custom_normal)

array1 = np.array(['iPhone: ', 'price: '])
array2 = np.array(['15', '$900'])

# perform element-wise array string concatenation
result = np.char.add(array1, array2)
print(result)


# Reshaping and initializing shapes
reshaped = np.arange(12).reshape(3, 4)  # 1D array reshaped to 3x4
init_like = np.zeros_like(reshaped)  # Array of zeros with the same shape as 'reshaped'
print("\nReshaped Array:\n", reshaped)
print("\nInitialized Like Reshaped:\n", init_like)