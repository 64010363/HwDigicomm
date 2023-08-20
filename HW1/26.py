#!/bin/python3
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

def bit_parity(bit):
    msg = ""
    parity = 0
    for i in range(0, 4):
        if bit // 2**(3 - i) % 2 == 1:
            msg += '1'
            parity += 1
        else:
            msg += '0'
    if parity % 2 == 1:
        msg += '1'
    else:
        msg += '0'
    return (msg)

def modulation(msg):
    t = np.arange(0, 0.25, 0.001)
    info = np.sin(np.arange(0, 0, 1))
    carrier = np.cos(2 * np.pi * 4 * t)
    for s in msg:
        if s == '1':
            mt = np.sin(2 * np.pi * 4 * t)
        else:
            mt = -1 * np.sin(2 * np.pi * 4 * t)
        res = np.multiply(carrier, mt)
        info = np.append(info, res)
    return (info)

num = 63
x1 = bit_parity(num // 10) + bit_parity(num % 10)
xt = modulation(x1)
T = np.arange(0, 2.5, 0.001)
plot.plot(T, xt)
plot.xlabel('Time (s)')
plot.ylabel('Amplitude (V)')
plot.title("Graph of " + str(num))
plot.grid(True, which='both')
plot.show()