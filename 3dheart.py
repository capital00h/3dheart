'''
=================================
3D heart shape in matplotlib
=================================
Demonstrates how to plot a 3D function in cartesian coordinates.
Uses the marching cubes algorithm in scikit-image to obtain a isosurface.
Example contributed by CAChemE.org
Adapted from: http://www.walkingrandomly.com/?p=2326
'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
from skimage import measure

# Set up mesh
n = 100

x = np.linspace(-4, 4, n)
y = np.linspace(-4, 4, n)
z = np.linspace(-4, 4, n)
X, Y, Z = np.meshgrid(x, y, z)



def f_heart(x, y, z):
    F = 320 * ((-x ** 2 * z ** 3 - 9 * y ** 2 * z ** 3 / 80) +
               (x ** 2 + 9 * y ** 2 / 4 + z ** 2 - 1) ** 3)
    return F



vol = f_heart(X, Y, Z)


verts, faces ,_ ,_ = measure.marching_cubes(vol, 0, spacing=(0.01, 0.01, 0.01))


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')


ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                cmap='Spectral', lw=1)

# Change the angle of view and title
ax.view_init(15, -15)

# ax.set_title(u"Made with ❤ (and Python)", fontsize=20) # if you have Python 3
ax.set_title('In \u2764\ufe0f with .py', fontsize=20)

# Show me some love ^^
plt.show()
