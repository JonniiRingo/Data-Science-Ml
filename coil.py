import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
mu0 = 4 * np.pi * 1e-7  # Permeability of free space

# Coil parameters
outer_diameter = 0.177  # meters
windings_radius = 0.063  # meters
current1 = 340000000  # amps for coil 1
current2 = -340000000  # amps for coil 2 (opposite direction)
frequency = 2516461  # Hz
voltage = 100000  # volts
impedance = 0.0300164  # ohms

# Derived parameters
cross_sectional_area = np.pi * (outer_diameter / 2)**2 - np.pi * windings_radius**2
current_density = current1 / cross_sectional_area

# Calculation grid
x = np.linspace(-0.2, 0.2, 40)  # Increased number of points
y = np.linspace(-0.2, 0.2, 40)  # Increased number of points
z = np.linspace(-0.2, 0.2, 40)  # Increased number of points
X, Y, Z = np.meshgrid(x, y, z)

# Initialize magnetic field arrays
Bx1 = np.zeros_like(X, dtype=np.float64)
By1 = np.zeros_like(Y, dtype=np.float64)
Bz1 = np.zeros_like(Z, dtype=np.float64)
Bx2 = np.zeros_like(X, dtype=np.float64)
By2 = np.zeros_like(Y, dtype=np.float64)
Bz2 = np.zeros_like(Z, dtype=np.float64)

# Helper function to calculate magnetic field of a toroidal coil
def calculate_magnetic_field(Bx, By, Bz, current, X, Y, Z):
    for i in range(X.shape[0]):
        for j in range(Y.shape[1]):
            for k in range(Z.shape[2]):
                r = np.sqrt(X[i, j, k]**2 + Y[i, j, k]**2 + Z[i, j, k]**2)
                if r == 0:
                    r = 1e-12  # avoid division by zero
                r_hat = np.array([X[i, j, k]/r, Y[i, j, k]/r, Z[i, j, k]/r])
                Idl = current_density * r * np.array([0, np.cos(frequency * 2 * np.pi * (r/windings_radius)), np.sin(frequency * 2 * np.pi * (r/windings_radius))]) * np.exp(1j * 2 * np.pi * frequency * r/windings_radius)
                B = (mu0 / (4 * np.pi)) * np.cross(Idl, r_hat) / r**2
                Bx[i, j, k] += B[0].real
                By[i, j, k] += B[1].real
                Bz[i, j, k] += B[2].real
    return Bx, By, Bz

# Calculate magnetic fields for both coils
Bx1, By1, Bz1 = calculate_magnetic_field(Bx1, By1, Bz1, current1, X, Y, Z - 0.00125)
Bx2, By2, Bz2 = calculate_magnetic_field(Bx2, By2, Bz2, current2, X, Y, Z + 0.00125)

# Adjust subsample rate here
subsample_rate = 2  # Decrease the subsample rate to show more vectors
subsample = (slice(None, None, subsample_rate), slice(None, None, subsample_rate), slice(None, None, subsample_rate))

# Plot the magnetic field in 3D
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the magnetic field vectors from the first coil (blue)
ax.quiver(X[subsample], Y[subsample], Z[subsample], Bx1[subsample], By1[subsample], Bz1[subsample], length=0.01, color='blue', normalize=True, label='Coil 1')

# Plot the magnetic field vectors from the second coil (red)
ax.quiver(X[subsample], Y[subsample], Z[subsample], Bx2[subsample], By2[subsample], Bz2[subsample], length=0.01, color='red', normalize=True, label='Coil 2')

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('3D Magnetic Field Vectors from Counter-Rotating Toroidal Coils')
ax.legend()

plt.show()
