"""
Constructing a cylinder and getting angles formed between it and plane
By running the code you can see the simple cylinder and angle between them

"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.linalg import norm

# axis and radius
p0 = np.array([1, 3, 2])  # point at one end
p1 = np.array([8, 5, 9])  # point at other end
R = 5

# vector in direction of axis
v = p1 - p0

# find magnitude of vector
mag = norm(v)

# unit vector in direction of axis
v = v / mag

# make some vector not in the same direction as v
not_v = np.array([1, 0, 0])
if (v == not_v).all():
    not_v = np.array([0, 1, 0])

# make vector perpendicular to v
n1 = np.cross(v, not_v)
# normalize n1
n1 /= norm(n1)

# make unit vector perpendicular to v and n1
n2 = np.cross(v, n1)

# surface ranges over t from 0 to length of axis and 0 to 2*pi
t = np.linspace(0, mag, 2)
theta = np.linspace(0, 2 * np.pi, 100)
rsample = np.linspace(0, R, 2)

# use meshgrid to make 2d arrays
t, theta2 = np.meshgrid(t, theta)

rsample, theta = np.meshgrid(rsample, theta)

# generate coordinates for surface
# "Tube"
X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta2) * n1[i] + R * np.cos(theta2) * n2[i] for i in [0, 1, 2]]
# "Bottom"
X2, Y2, Z2 = [p0[i] + rsample[i] * np.sin(theta) * n1[i] + rsample[i] * np.cos(theta) * n2[i] for i in [0, 1, 2]]
# "Top"
X3, Y3, Z3 = [p0[i] + v[i] * mag + rsample[i] * np.sin(theta) * n1[i] + rsample[i] * np.cos(theta) * n2[i] for i in
              [0, 1, 2]]

ax = plt.subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='blue')
ax.plot_surface(X2, Y2, Z2, color='blue')
ax.plot_surface(X3, Y3, Z3, color='blue')

# Angle formed between rigid body and the Standard basis
mag_p0 = norm(p0)
mag_p1 = norm(p1)

product_mag = mag_p1 * mag_p1
dot_product = ((p0[0] * p1[0]) + (p0[1] * p1[1]) + (p0[2] * p1[2]))

angle = np.arccos(dot_product / product_mag)
print('product_mag = ', product_mag)
print('dot_product = ', dot_product)
print('Theta = ', angle)
