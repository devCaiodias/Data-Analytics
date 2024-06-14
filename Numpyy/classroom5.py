import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([1,2,3,4])
# print(arr3 + arr1)

arr3 = np.array([[1,2,3], [4,5,6]])
print(arr3 + arr1)
print(arr3 * arr1)

x = np.arange(4)
xx = x.reshape(4, 1)
y = np.ones(5)
z = np.ones((3, 4))

# Não é possivel
# x + y

print((xx + y).shape)
print((xx + y))

print((x + z).shape)
print((x + z))

# Execicio
np.random.seed(42)
a = np.random.random(size=3)
b = np.random.random(size=3)


diferencia = a - b

euclides = np.sqrt(np.sum(diferencia ** 2))
print(euclides)