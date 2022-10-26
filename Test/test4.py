import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X, Y = np.meshgrid(np.arange(10), np.arange(10))
Z = np.sin(X) + np.sin(Y)
x = X.flatten()
y = Y.flatten()
z = Z.flatten()

fig = plt.figure(figsize=(9, 3.2))
plt.subplots_adjust(0, 0.07, 1, 1, 0, 0)
ax = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
ax.set_title("trisurf with color acc. to z")
ax2.set_title("surface with color acc. to x")

ax.plot_trisurf(x, y, z,  cmap="magma")

colors = plt.cm.magma((X-X.min())/float((X-X.min()).max()))
ax2.plot_surface(X, Y, Z, facecolors=colors, linewidth=0, shade=False)

ax.set_xlabel("x")
ax2.set_xlabel("x")
plt.show()
