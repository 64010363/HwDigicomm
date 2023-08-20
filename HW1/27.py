#!/bin/python3
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

t = np.arange(0, 5, 0.001)
x1 = np.cos(2 * np.pi * 6 * t)
x2 = np.cos(2 * np.pi * 3 * t)
xt = np.add(x1, x2)
plot.plot(t, xt)
plot.xlabel('Time (s)')
plot.ylabel('Amplitude (V)')
plot.title("Graph")
plot.grid(True, which='both')
plot.show()