#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 4, 0.01)
x_sin = np.sin(4 * 2 * np.pi * t)
x_cos = np.cos(4 * 2 * np.pi * t)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(t, x_sin, 'g')
axes[0].grid(True)
axes[0].set_title("sin function")
axes[1].plot(t, x_cos, 'g')
axes[1].grid(True)
axes[1].set_title("cosin function")
plt.show()