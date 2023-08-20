#!/bin/python3
import numpy as np

A = np.array([[1, 4, 5, 12, 14],
                [-5, 8, 9, 0, 17],
                [-6, 7, 11, 19, 21]])
print(A[:2, :3]) # two rows, three columns
print(A[:1, :4]) #one row, four columns
print(A[:3, :2]) #one row, four columns