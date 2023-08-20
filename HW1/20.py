#!/bin/python3
import numpy as np
import math

signal_power = [8, 10]
noise_power = [2, 2]
snr = np.divide(signal_power, noise_power)
print(snr)

snr_dB = []
for i in snr:
    snr_dB.append(10 * math.log10(i))