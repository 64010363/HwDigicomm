#!/bin/python3
import numpy as np
import matplotlib.pyplot as plot

t = np.arange(0, 4, 0.01)
x_cos = np.cos(4 * 2 * np.pi * t)

plot.plot(t, x_cos)
plot.title("Cosine waves of 4Hz")
plot.xlabel("Time (sec)")
plot.ylabel("x(t)")
plot.grid(True, which='both')
plot.show()