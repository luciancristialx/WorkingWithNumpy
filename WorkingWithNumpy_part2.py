import numpy as np

a = np.arange(0,21)
print(a)

print("Print the 9th element: ", a[8] , "\n")
print("Print the last element: ", a[-1] , "\n")

print("Slicing: ", a[:10], "\n")
print("Slicing_part2: ", a[10:], "\n")

b = a[5:15] = 40
print("Changes in list: ", a, "\n")

c = a.copy()
print("Original copy of list a: ", c, "\n")
c[5:15] = 40
print("Changes in copy: ", c, "\n")

d = np.arange(25).reshape(5,5)
print("Print 2D array:\n------------------\n", d, "\n")

print("Print value by accessing the value using i, j as indexes: d[i = row][j = column]", d[2][2], "\n")
print("Print value by accessing the value using i, j as indexes: d[i = row][j = column]", d[4][2], "\n")
print("Slicing 2D array version1: \n", d[0:2,2:], "\n")
print("Slicing 2D array version2: \n", d[1:4,1:4], "\n")

e = np.arange(1,20)
print("Print 1D array: \n", e, "\n")
print("Conditional selection version1: ->\n", e[e > 12], "\n")
print("Conditional selection version2: ->\n", e[e % 4], "\n")

# f = np.arange(10) -> 1D array
# g = np.arange(10,20) -> 1D array

f = np.arange(12).reshape(3,4)
g = np.arange(10,22).reshape(3,4)
print("--------------------\nOperations on Numpy:\n--------------------\n")
h = f + g
print("Add:\n",h)
print("Max of f list: ",np.max(f))



