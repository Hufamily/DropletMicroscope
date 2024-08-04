# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:35:34 2024

@author: Ethan Hu
"""
import matplotlib.pyplot as plt
import numpy as np
ExpData = [0.002664645, 0.003194563,0.003360272,0.0036999,0.003711925]
Error = [0.0000552325,0.0001353,0.000107077,0.000163119,0.000144617]

plt.scatter([0,0,0,0,0], ExpData, color = 'b', label = 'Experimental Focal Lengths')
plt.errorbar([0,0,0,0,0], ExpData, yerr=Error, ls = 'none', ecolor = 'b')

plt.scatter([0,0],[0.002888187968, 0.008635372628], color = 'r', label = 'Predicted Focal Range')
plt.errorbar([0,0], [0.002888187968, 0.008635372628],yerr = [0.000073034638,0.000218365745], ls = 'none', ecolor = 'r')

plt.legend()
plt.ylabel('Focal Length (m)')