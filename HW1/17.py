#!/bin/python3
import numpy as np

A = np.array([[2, 4], [5, -6]])
print(A)
B = np.array([[9, -3], [3, 6]])
C = A + B # element wise addition
print(C)
#matrix add 'integer'
C1 = A + 5
print(C1)