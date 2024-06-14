import numpy as np

np.random.seed(42)
arr = np.random.randint(0, 100, size=10)
# print(arr)
# print(arr > 50)
# print((arr > 50) & (arr < 75))
# print(arr[(arr > 50) & (arr < 75)])
# print(np.where((arr > 50) & (arr < 75), "Papai noel é Top", "Papai noel é Feio"))
# arr[(arr > 50) & (arr < 75)] = -1
# print(arr)

np.random.seed(42)
arr = np.random.randint(0, 100, size=10)
print(arr)
print((arr > 50) & (arr < 75))

print(all((arr > 50) & (arr < 75)))
print(np.all((arr > 50) & (arr < 75)))

print(any((arr > 50) & (arr < 75)))
print(np.any((arr > 50) & (arr < 75)))

print(arr.reshape(2, 5) < 70)
print(np.all(arr.reshape(2, 5) < 70))
print(np.all(arr.reshape(2,5) < 70, axis=0))

print(arr.reshape(2, 5))
print(arr.reshape(2,5) > np.array([20,30,40,50,60 ]))