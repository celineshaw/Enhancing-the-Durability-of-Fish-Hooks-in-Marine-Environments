#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 08:28:25 2024

@author: celineshaw
"""

import matplotlib.pyplot as plt
import numpy as np

def print_circuit():
    circuit = """
    Cu | Cu2+ || Salt bridge || Reference electrode
    """
    print("Equivalent Electrical Circuit Model for a Simple Corroding Electrode:")
    print(circuit)

# Given data
Rs = 50.00  # Solution Resistance (Ohm)
Rct = 3500.00  # Charge Transfer Resistance (Ohm)
CPE = 1e-6  # Capacitive Behavior (Farads or CPE Unit)

# Simulated frequency values
frequencies = np.logspace(5, -2, 100)  # Frequency range from 100 kHz to 0.01 Hz

# Calculate Z' and Z'' for each frequency
Z_prime = Rct / (1 + (2 * np.pi * frequencies * Rct * CPE)**2)
Z_double_prime = (Rct**2) * (2 * np.pi * frequencies * CPE) / (1 + (2 * np.pi * frequencies * Rct * CPE)**2)

# Create the Nyquist plot
plt.figure(figsize=(8, 8))
plt.plot(Rs + Z_prime, Z_double_prime, 'o-', label='Simulated EIS Data', markersize=3)

# Label Rs and Rs+Rct points
plt.plot(Rs, 0, 's', label='Rs', markersize=8, color='red')  # Solution resistance point
plt.plot(Rs + Rct, 0, 's', label='Rs+Rct', markersize=8, color='green')  # Total resistance at low frequency

# Annotations for Rs and Rs+Rct
plt.annotate('Rs', (Rs, 0), textcoords="offset points", xytext=(-15,-15), ha='center', color='red')
plt.annotate('Rs+Rct', (Rs + Rct, 0), textcoords="offset points", xytext=(-15,-15), ha='center', color='green')

plt.xlabel('Real Impedance (Z\') [Ohm]')
plt.ylabel('Imaginary Impedance (Z\'\') [Ohm]')
plt.title('Nyquist Plot for a Simple Corroding Electrode')
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.show()

# Print the equivalent circuit model
print_circuit()