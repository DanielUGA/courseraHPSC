"""
Demonstration script for quadratic interpolation.
Just need to figure how to relate xi and A
Modified by: ** Ryan (Weiran) Zhao **
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve

# Set up linear system to interpolate through data points:

# Data points:
xi = np.array([-1., 1., 2])
yi = np.array([0., 4., 3.])

# It would be better to define A in terms of the xi points.
# Doing this is part of the homework assignment.
A = np.array([np.ones(3),xi,xi*xi]).T
b = yi

# Solve the system:
c = solve(A,b)

print "The polynomial coefficients are:"
print c

# Plot the resulting polynomial:
x = np.linspace(-2,4,1001)   # points to evaluate polynomial
y = c[0] + c[1]*x + c[2]*x**2

plt.figure(1)       # open plot figure window
plt.clf()           # clear figure
plt.plot(x,y,'b-')  # connect points with a blue line

# Add data points  (polynomial should go through these points!)
plt.plot(xi,yi,'ro')   # plot as red circles
plt.ylim(-1,5)         # set limits in y for plot

plt.title("Data points and interpolating polynomial")

plt.savefig('hw2a.png')   # save figure as .png file
