import numpy as np

# x=[[1,2,3],[4,5,6],[7,8,9]]
# print(x)

# x=[[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]]]
# y = np.array(x)
# print(y)

a = [1,2,3,4,5] #1D list
b = [[1,2,3],[4,5,6],[7,8,9]] # 2D list (square matrix no of rows = no of columns)

a = np.array(a)
b = np.array(b)

print(a,"\n","----------")
print(b,"\n","----------")
print("Max: ", a.max(), "\n","----------")
print("Max: ", a.min(), "\n","----------")
print("Index of max value: ", a.argmax(), "\n","----------")

# 1. Zero matrix (all elements are = 0)
c=np.zeros((3,2)) + 5
print(c,"\n","----------\n")

# 2. Unity matrix (all elements are equal)
d=np.ones((3,2))
print(d,"\n","----------\n")

# 3. Identity matrix (all elements on the left diagonal are = 1)
e=np.eye(3)
print(e,"\n","----------\n")

f = np.arange(3,10)
print(f,"\n","----------\n")

g = np.arange(50).reshape(5,10)
print(g,"\n","----------\n")

h = np.linspace(0,10,5) # 5 elements for 0->10 (linear space)
print(h,"\n","----------\n")

i = np.random.rand(5)
print(i,"\n","----------\n")

j = np.random.randint(100)
print(j,"\n","----------\n")



