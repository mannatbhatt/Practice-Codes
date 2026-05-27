import numpy as np
import matplotlib.pyplot as plt

def donut(a, b, phi, theta):
    x = (a + b * np.cos(theta)) * np.cos(phi)
    y = (a + b * np.cos(theta)) * np.sin(phi)
    z = b * np.sin(theta)
    return x, y, z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a, b = 1, 2
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)

x_coords = []
y_coords = []
z_coords = []

for phi in u:
    for theta in v:
        x, y, z = donut(a, b, phi, theta)
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)

ax.scatter(x_coords, y_coords, z_coords, c=z_coords, cmap='viridis', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

