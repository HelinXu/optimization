# % Please forward any comments or bug reports in chat
# Copyright 2021. INDUSMIC PRIVATE LIMITED.THERE IS NO WARRANTY, EXPRESS OR IMPLIED. WE DO NOT ASSUME ANY LIABILITY FOR THE USE OF THIS PROGRAM. If software is modified to produce derivative works, such modified software should be clearly marked. Additionally, user can redistribute it and/or modify it under the terms of the GNU General Public License. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY. See the GNU General Public License for more details.
# % for any support connect with us on help.indusmic@gmail.com
# % Author: Sakshi Chadda

from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import meshgrid
import matplotlib.pyplot as plt

def objective(x, y):
 return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * 
  pi * x)+cos(2 * pi * y))) + e + 20


r_min, r_max = -32.768, 32.768
xaxis = arange(r_min, r_max, 2.0)
yaxis = arange(r_min, r_max, 2.0)
x, y = meshgrid(xaxis, yaxis)
results = objective(x, y)
figure = plt.figure()
axis = figure.gca( projection='3d')
axis.plot_surface(x, y, results, cmap='jet', shade= "false")
plt.show()
plt.contour(x,y,results)
plt.show()
plt.scatter(x, y, results)
plt.show()
