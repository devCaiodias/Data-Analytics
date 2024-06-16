import numpy as np

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.concatenate([a, b]))
# print(np.concatenate([a, b], axis=0))

# a = np.array([[1,2,3]])
# b = np.array([[4,5,6]])
# print(np.concatenate([a, b]))
# print(np.concatenate([a, b], axis=1))

# VSTACK:

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.vstack([a,b]))

# a = np.array([[1,2,3]])
# b = np.array([[4,5,6]])
# print(np.vstack([a, b]))

# a = np.array([[1,2,3], [4, 5, 6]])
# b = np.array([[7,8,9], [10,11,12]])
# print(np.vstack([a, b]))

# # a = np.array([[1,2,3], [4, 5, 6]])
# # b = np.array([[7], [10]])
# # print(a + b)
# # # print(np.vstack([a, b]))

# a = np.array([[1,2,3], [4, 5, 6]])
# b = np.array([[7, 8, 9]])
# print(np.vstack([a, b]))

# HSTACK:

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.hstack([a, b]))

# a = np.array([[1,2,3]])
# b = np.array([[4,5,6]])
# print(np.hstack([a, b]))

# a = np.array([[1,2,3], [4, 5, 6]])
# b = np.array([[7,8,9], [10,11,12]])
# print(np.hstack([a, b]))

# a = np.array([[1,2,3], [4, 5, 6]])
# b = np.array([[7, 8, 9]])
# print(np.hstack([a, b]))

# a = np.array([[1,2,3], [4, 5, 6]])
# b = np.array([[7], [10]])
# print(np.hstack([a, b]))

# Append

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.append(a, b))

a = np.array([[1,2,3]])
b = np.array([[4,5,6]])
print(np.append(a, b))

a = np.array([[1,2,3], [4, 5, 6]])
b = np.array([[7,8,9], [10,11,12]])
print(np.append(a, b))

a = np.array([[1,2,3], [4, 5, 6]])
b = np.array([[7,8], [10,11]])
print(np.append(a, b))


# print(a, a.flatten())