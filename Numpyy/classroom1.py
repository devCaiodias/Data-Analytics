import numpy as np

arry = np.array([1,2,3])
print(arry.dtype, arry)

arry = np.array([1,2,3])
arry = arry.astype("float")
print(arry.dtype, arry)

arry = np.array([1,2,3], dtype=np.uint8)
print(arry.dtype, arry)

arry = np.array(["Olá", 2.1, [2,3,4]], dtype="object")
print(arry.shape)