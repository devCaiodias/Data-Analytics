import pandas as pd
import numpy as np

np.random.seed(42)

serie1 = pd.Series(data=np.random.normal(size=5))
serie2 = pd.Series(data=np.random.normal(size=5), index=np.arange(4, -1, -1))
serie3 = pd.Series(data=np.random.normal(size=5), index=np.arange(10, 15))
serie4 = pd.Series(data=np.random.normal(size=5), index=np.arange(4, 9))
# print(serie1)
# print(serie2)
# print(serie3)

# Soma
# print(serie1 + serie2)
# print(serie1 + serie4)
# print(serie1 + 2)
# print(serie1.add(serie2))
# print(serie1.add(np.array([1,2,3,4,5])))
# print(serie1.add(serie4, fill_value=0))

# Subtração

# print(serie1 - serie2)
# print(serie1.sub(serie2))

# Multiplicar

# print(serie1 * serie2)
# print(serie1 * serie4)
# print(serie1.mul(serie2))

# Multiplicar (produto vetorial)

# print(serie1.dot(serie2))

# Divisão

# print(serie1 / serie2)
# print(serie1.div(serie2))

# Exponenciação

print(serie1 ** serie2)
print(serie1.pow(serie2))