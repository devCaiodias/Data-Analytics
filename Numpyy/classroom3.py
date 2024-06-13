import numpy as np

arry = np.array([1,2,3])
arry[2] = 4
print(arry)
arry[1] = 1.5844
print(arry)
arry[1] = "3"
print(arry)

a = np.arange(12, dtype='int64')
b = a.reshape(3,4)
c = a[::2]
print(a)
print(b)
print(c)

print(f"a: dtype={a.dtype} / shape:{a.shape} / size:{a.size} / itemsize:{a.itemsize} / strides:{a.strides}")
print(f"b: dtype={b.dtype} / shape:{b.shape} / size:{b.size} / itemsize:{b.itemsize} / strides:{b.strides}")

print(f"a: dtype={a.dtype} / shape:{a.shape} / size:{a.size} / itemsize:{a.itemsize} / strides:{a.strides}")
print(f"c: dtype={c.dtype} / shape:{c.shape} / size:{c.size} / itemsize:{c.itemsize} / strides:{c.strides}")

def mudar_a(a):
    a[1] = 1200
print(a)
mudar_a(a)
print(a) 
print(b) 
print(c) 