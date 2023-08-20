#!/bin/python3
import numpy as np

SS = np.array([1, 3, 5, 7, 9, 7, 5])
# 3rd to 5th elements
print(SS[2:5]) # Output: [5, 7, 9]
# 1st to 4th elements
print(SS[:-5]) # Output: [1, 3]
# 6th to last elements
print(SS[5:]) # Output:[7, 5]
# 1st to last elements
print(SS[:]) # Output:[1, 3, 5, 7, 9, 7, 5]
# reversing a list
print(SS[::-1]) # Output:[5, 7, 9, 7, 5, 3, 1]