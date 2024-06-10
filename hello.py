import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function for a catenoid
def f(u, v):
    x = np.cosh(v/10) * np.cos(u)  # Adjust the diameter here
    y = np.cosh(v/10) * np.sin(u)  # Adjust the diameter here
    z = v
    return x, y, z

# Create a grid of points on which to evaluate the function
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(-1, 1, 100)
u, v = np.meshgrid(u, v)

# Evaluate the function on the grid
x, y, z = f(u, v)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the catenoid
ax.plot_surface(x, y, z, color='blue', alpha=0.5)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set title
ax.set_title('Wormhole')

# Show the plot
plt.show()
