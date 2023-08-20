#!/bin/python3
import numpy as np
import matplotlib.pyplot as plot

t = np.arange(0, 4, 0.01)
x_sin = np.sin(4 * 2 * np.pi * t)

plot.plot(t, x_sin)
plot.title("Sine waves of 4Hz")
plot.xlabel("Time (sec)")
plot.ylabel("x(t)")
plot.grid(True, which='both')
plot.show()