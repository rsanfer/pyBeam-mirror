#!/usr/bin/env python
#
# pyBeam, a Beam Solver
#
# Copyright (C) 2018 Ruben Sanchez, Rocco Bombardieri, Rauno Cavallaro
# 
# Developers: Ruben Sanchez (SciComp, TU Kaiserslautern)
#             Rocco Bombardieri, Rauno Cavallaro (Carlos III University Madrid)
#
# This file is part of pyBeam.
#
# pyBeam is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# pyBeam is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero
# General Public License along with pyBeam.
# If not, see <http://www.gnu.org/licenses/>.
#

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys, os
from pyBeamLib import pyBeamSolver

# Load running directory
file_dir = os.path.dirname(os.path.realpath(__file__))

beam = pyBeamSolver(file_dir ,'config_NL.cfg')

Lift = 6980.7 #20942/3 # [N]

beam.SetLoads(19,0,0,Lift)

#beam.SetLoads(39,0,0,5000)

beam.Run()

beam.PrintDisplacements(1)

beam.PrintDisplacements(19)

#for i in range(beam.nElem):
#   beam.Debug_Print(i)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create cubic bounding box to simulate equal aspect ratio
max_range = np.array([np.amax(beam.coordinate_X0) - np.amin(beam.coordinate_X0), np.amax(beam.coordinate_Y0) - np.amin(beam.coordinate_Y0),
                      np.amax(beam.coordinate_Z0) - np.amin(beam.coordinate_Z0)]).max()
Xb = 0.5 * max_range * np.mgrid[-1:2:2, -1:2:2, -1:2:2][0].flatten() + 0.5 * (
            np.amax(beam.coordinate_X0) + np.amin(beam.coordinate_X0))
Yb = 0.5 * max_range * np.mgrid[-1:2:2, -1:2:2, -1:2:2][1].flatten() + 0.5 * (
            np.amax(beam.coordinate_Y0) + np.amin(beam.coordinate_Y0))
Zb = 0.5 * max_range * np.mgrid[-1:2:2, -1:2:2, -1:2:2][2].flatten() + 0.5 * (
            np.amax(beam.coordinate_Z0) + np.amin(beam.coordinate_Z0))
# Comment or uncomment following both lines to test the fake bounding box:
for xb, yb, zb in zip(Xb, Yb, Zb):
    plt.plot([xb], [yb], [zb], 'w')

plt.plot(beam.coordinate_X[0:20], beam.coordinate_Y[0:20], beam.coordinate_Z[0:20],'b')
plt.plot(beam.coordinate_X0[0:20], beam.coordinate_Y0[0:20], beam.coordinate_Z0[0:20],'g')
rigid = 80

for i in range(19,19+rigid):
    node_i = int(beam.elem_py[i].GetNodes()[0, 0] - 1)
    node_j = int(beam.elem_py[i].GetNodes()[1, 0] - 1)
    plt.plot([ beam.coordinate_X[node_i],beam.coordinate_X[node_j] ], [ beam.coordinate_Y[node_i],beam.coordinate_Y[node_j] ], [ beam.coordinate_Z[node_i],beam.coordinate_Z[node_j] ],'b')
    plt.plot([ beam.coordinate_X0[node_i],beam.coordinate_X0[node_j] ], [ beam.coordinate_Y0[node_i],beam.coordinate_Y0[node_j] ], [ beam.coordinate_Z0[node_i],beam.coordinate_Z0[node_j] ],'g')



plt.xlabel('X')
plt.ylabel('Y')
plt.show()

