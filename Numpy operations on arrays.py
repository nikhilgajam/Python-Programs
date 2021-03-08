import numpy as np

print("===> 1D\n")
# Creating a 1 Dimensional numpy array
arr1D = np.array([10, 20, 30, 40])
print(arr1D)

# Accessing 1D numpy array
print(arr1D[3])

# Using arithmetic operators on 1D numpy arrays
print(arr1D[1] * arr1D[3])

print("\n===> 2D\n")
# Creating a 2 Dimensional numpy array
arr2D = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(arr2D)

# Accessing 2D numpy array
print(arr2D[0, 3])

# Using arithmetic operators on 2D numpy arrays
print(arr2D[1, 2] * arr2D[0, 2])


print("\n===> 3D\n")
# Creating a 3 Dimensional numpy array
arr3D = np.array([[[10, 20, 30], [40, 50, 60], [70, 80, 90]]])
print(arr3D)

# Accessing 3D numpy array
print(arr3D[0, 1, 2])

# Using arithmetic operators on 3D numpy arrays
print(arr3D[0, 1, 0] * arr3D[0, 0, 0])


print("\n===> 4D\n")
# Creating a 4 Dimensional numpy array
arr4D = np.array([[[[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 1000]]]])
print(arr4D)

# Accessing 4D numpy array
print(arr4D[0, 0, 0, 1])

# Using arithmetic operators on 4D numpy arrays
print(arr4D[0, 0, 0, 1] / arr4D[0, 0, 1, 1])

print("\n===> Slicing operations on numpy arrays\n")
# Slicing operations on numpy arrays
print(arr1D[0:3])
print(arr1D[:2])
print(arr1D[1:])
print(arr1D[0:3:2])
print(arr1D[-3:-1])
print(arr2D[1, 1:4])


print("\n===> Data types in numpy\n")
# Data types in numpy search for data types in arrays. Ex: i, S, O, c etc

print(arr1D.dtype)
arr = np.array(arr1D, dtype='S')
print(arr.dtype)
print(arr)

# astype()
arr = arr.astype('i')
print(arr)

# copy()
arr_c = arr1D.copy()   # It creates another numpy array with existing data, So it will not change the data if we change the original or copy
print(arr)

# view()
arr_v = arr1D.view()   # It is like a pointer to an array, the original data will be changed if we change from view created array
print(arr)

# base()
print(arr_c.base)
print(arr_v.base)

# shape()
print(arr1D.shape)
print(arr4D.shape)
arr = np.array([[1, 2, 3], [4, 5, 6], [7]])  # Shape attribute with jagged array will not show all dimensions
print(arr.shape)

# reshape()
print(arr1D.reshape(2, 2))
print(arr4D.reshape(-1))  # -1 will make any array to 1D array

# concatenate()
arr = np.concatenate([arr1D, arr1D, arr1D])  # Concatenate 2 or more numpy arrays
print(arr)

# array_split()
arr = np.array_split(arr1D, 3)
print(arr)

# where()
print(np.where(arr1D == 40))


print("\n===> Iterating numpy array\n")
# Using nditer()
for i in np.nditer(arr4D):
    print(i, end=" ")

print()

# Using loops
for i in arr2D:
    for j in i:
        print(j, end=" ")


print("\n===> Statistical operations\n")
# Statistical operations on numpy array
x = np.array([1, 2, 3, 4, 5, 6, 7, 160, 100])


print("Max:", np.max(x))
print("Min:", np.min(x))
print("Sum:", np.sum(x))
print("Product:", np.prod(x))
print("Mean:", np.mean(x))
print("Standard Deviation:", np.std(x))
print("Variance:", np.var(x))











