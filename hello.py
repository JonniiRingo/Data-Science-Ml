import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the wormhole
a = 2  # Stretch along the z-axis
b = 0.5  # Throat size

# Parameters for the toroids
R_toroid = 2.5  # Major radius (from the center of the toroid to the center of the tube)
r_toroid = 0.5  # Minor radius (radius of the tube)

# Generate mesh grid for the wormhole
z = np.linspace(-10, 10, 400)  # z coordinates
theta = np.linspace(0, 2 * np.pi, 100)  # Angular coordinates
Z, Theta = np.meshgrid(z, theta)

# Compute radial distance r
R = np.sqrt(b**2 + (Z/a)**2)

# Compute Cartesian coordinates for the wormhole
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Generate mesh grid for the toroids
phi = np.linspace(0, 2 * np.pi, 100)
phi, Theta_toroid = np.meshgrid(phi, theta)

# Compute Cartesian coordinates for the toroids wrapping around the wormhole
# Toroid 1
X_toroid1 = (R_toroid + r_toroid * np.cos(phi)) * np.cos(Theta_toroid)
Y_toroid1 = (R_toroid + r_toroid * np.cos(phi)) * np.sin(Theta_toroid)
Z_toroid1 = r_toroid * np.sin(phi) - b

# Toroid 2
X_toroid2 = (R_toroid + r_toroid * np.cos(phi)) * np.cos(Theta_toroid)
Y_toroid2 = (R_toroid + r_toroid * np.cos(phi)) * np.sin(Theta_toroid)
Z_toroid2 = r_toroid * np.sin(phi) + b

# Combine the coordinates
X_combined = np.concatenate((X, X_toroid1, X_toroid2), axis=0)
Y_combined = np.concatenate((Y, Y_toroid1, Y_toroid2), axis=0)
Z_combined = np.concatenate((Z, Z_toroid1, Z_toroid2), axis=0)

# Plot the combined object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='b', alpha=0.7, rstride=10, cstride=10, edgecolor='k', linewidth=0.5)
ax.plot_surface(X_toroid1, Y_toroid1, Z_toroid1, color='r', alpha=0.6, rstride=5, cstride=5, edgecolor='k', linewidth=0.5)
ax.plot_surface(X_toroid2, Y_toroid2, Z_toroid2, color='r', alpha=0.6, rstride=5, cstride=5, edgecolor='k', linewidth=0.5)

# Set plot labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Wormhole Visualization with Wrapping Toroids')

# Show the plot
plt.show()
