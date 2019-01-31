import numpy as np
from numpy.linalg import inv
from tinydb import TinyDB,Query


m=3
w = np.empty((m, m))
print(w)
for i in range(0, m, 1):
    w[i][i] = float(input("enter the weight:"))
    print(w[i][i])
print(w)