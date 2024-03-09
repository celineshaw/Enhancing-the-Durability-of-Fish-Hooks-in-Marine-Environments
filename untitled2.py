#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:09:58 2024

@author: celineshaw
"""

import vtk

# Create a rendering window and renderer
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

# Create a render window interactor
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Create the main body of the hook (a torus)
torus = vtk.vtkParametricTorus()
torus.SetRingRadius(1.0)
torus.SetCrossSectionRadius(0.1)

torusSource = vtk.vtkParametricFunctionSource()
torusSource.SetParametricFunction(torus)
torusSource.Update()

torusMapper = vtk.vtkPolyDataMapper()
torusMapper.SetInputConnection(torusSource.GetOutputPort())

torusActor = vtk.vtkActor()
torusActor.SetMapper(torusMapper)

# Create the pointed end of the hook (a cone)
cone = vtk.vtkConeSource()
cone.SetRadius(0.1)
cone.SetHeight(0.5)
cone.SetDirection(-1, -1, 0)  # Pointing in a direction to appear like a hook
cone.SetResolution(30)
cone.Update()

coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)
coneActor.SetPosition(0.9, -0.9, 0)  # Position it at the end of the torus

# Add the actors to the renderer
renderer.AddActor(torusActor)
renderer.AddActor(coneActor)

# Set the background color
renderer.SetBackground(0.1, 0.2, 0.4)  # Dark blue

# Render and start the interaction
renderWindow.Render()
renderWindowInteractor.Start()