#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:09:55 2024

@author: celineshaw
"""
# Constants (example values, replace with your actual parameters)
beta_a = 0.12  # Anodic Tafel slope in volts
beta_c = 0.12  # Cathodic Tafel slope in volts
B = beta_a * beta_c / (beta_a + beta_c)  # Stern-Geary constant

# Assuming you've calculated the slope (b) of the linear region
# and the corrosion potential (E_corr) from your data
b = 0.01  # Slope of the linear region (ohm*m^2), replace with your actual value
E_corr = -0.2  # Corrosion potential in volts, replace with your actual value

# Calculate polarization resistance (R_p) and corrosion current density (i_corr)
R_p = 1 / b  # Polarization resistance (ohm*m^2)
i_corr = B / R_p  # Corrosion current density (A/m^2)

# Display the polarization resistance and corrosion current density
print(f"Polarization Resistance (R_p): {R_p} ohm*m^2")
print(f"Corrosion Current Density (i_corr): {i_corr} A/m^2")