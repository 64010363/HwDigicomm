#!/bin/python3
import math

signal_power = 8
noise_power = 2
snr = signal_power / noise_power
snr_dB = 10 * math.log10(snr)
print(snr)
print(snr_dB)