#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:47:54 2024

@author: celineshaw
"""

## FIXME


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters analogous to the MATLAB code
shank_length = 5
shank_radius = 0.05
barb_length = 0.5
eye_major_radius = 0.2
eye_minor_radius = 0.05

# Straight shank
shank_x, shank_y = np.meshgrid(np.linspace(-shank_length/2, shank_length/2, 100),
                               np.linspace(-shank_radius, shank_radius, 10))
shank_z = np.zeros_like(shank_x)

# Barb as a triangle
barb_x = [0, barb_length, barb_length, 0]
barb_y = [2*shank_radius, 2*shank_radius, 2.5*shank_radius, 2*shank_radius]
barb_z = [0, 0, 0, 0]

# Eye of the hook as a torus segment
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
eye_x = (eye_major_radius + eye_minor_radius*np.cos(theta)) * np.cos(phi)
eye_y = (eye_major_radius + eye_minor_radius*np.cos(theta)) * np.sin(phi)
eye_z = eye_minor_radius * np.sin(theta)

# Generate random corrosion data
shank_corrosion = np.random.rand(*shank_x.shape)
barb_corrosion = np.random.rand(len(barb_x))
eye_corrosion = np.random.rand(*eye_x.shape)

# Plot the straight shank with corrosion data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
shank_plot = ax.plot_surface(shank_x, shank_y, shank_z, facecolors=plt.cm.jet(shank_corrosion), linewidth=0)
plt.colorbar(shank_plot)
plt.title('Straight Shank with Corrosion Data')
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.axis('equal')
plt.show()

# Plot the barb with corrosion data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
barb_plot = ax.fill(barb_x, barb_y, barb_z, c=barb_corrosion, cmap=plt.cm.jet)
plt.colorbar(barb_plot[0])
plt.title('Barb with Corrosion Data')
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.axis('equal')
plt.show()

# Plot the eye with corrosion data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
eye_plot = ax.plot_surface(eye_x, eye_y - shank_length/2 - eye_major_radius, eye_z, facecolors=plt.cm.jet(eye_corrosion), linewidth=0)
plt.colorbar(eye_plot)
plt.title('Eye with Corrosion Data')
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.axis('equal')
plt.show()
