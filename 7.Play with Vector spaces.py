# Play with Vector Spaces

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# For visualizing Each Scenarios

# The 3D vector V

v = [1, 2, 3]

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.set_xlim([0, 10])
ax.set_ylim([-1, 10])
ax.set_zlim([0, 10])
ax.set_xlabel(r'X')
ax.set_ylabel(r'Y')
ax.set_zlabel(r'Z')
ax.set_title('Vector V in 3D')
start = [0, 0, 0]
# x_basis = [1,0,0]
# y_basis = [0,1,0]
# z_basis = [0,0,1]

# To Represent Standard Basis
ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2])
x_std_basis = [1, 0, 0]
y_std_basis = [0, 2, 0]  # consider[0,1,0]+[0,1,0]
z_std_basis = [0, 0, 3]  # consider[0,0,1]+[0,0,1]+[0,0,1]

ax.quiver(start[0], start[1], start[2], x_std_basis[0], x_std_basis[1], x_std_basis[2], color='red')
ax.quiver(x_std_basis[0], x_std_basis[1], x_std_basis[2], y_std_basis[0], y_std_basis[1], y_std_basis[2], color='green')
ax.quiver(x_std_basis[0], y_std_basis[1], y_std_basis[2], z_std_basis[0], z_std_basis[1], z_std_basis[2], color='black')

plt.show()


# To Check weather Linear of Not

def T(V):
    W = np.zeros((3, 1))
    W[0, 0] = V[0, 0] + V[1, 0]
    W[1, 0] = 0
    W[2, 0] = V[2, 0] + V[0, 0]
    return W


V = np.array([[1], [2], [3]])
W = T(V)

U = np.array([[-1], [3], [1]])
V = np.array([[3], [1], [4]])
k = 7

print('V = \n', V, '\n\n', 'W = \n', W)
print('\n\nT(k*V) = \n', T(k * V), '\n')
print('k*T(V) =\n', k * T(V), '\n')
print('T(U+V) = \n', T(U + V), '\n')
print('T(U)+T(V) = \n', T(U) + T(V))

"""
[v1,v2,v3] = [v1 + v2, 0, v3+v1]
Applying oru V vector for v1,v2,v3 and verifying for the Linear or Non-linear
T(kV) = kT(V)........(1)
T(U+V) = T(U)+T(V).....(2)
if (1) and (2) satisfies its linear of its Non-linear
By running the above code You can See the result for the both equation 1 and 2 
we can see the above vector for the given condition is linear
"""

""" 
As a vector in 3d space has infinite perpendicular vector to its, plotting
it and commenting its surface was difficult for me
"""

""" 
And also I have constructed Standard basis for v.

#The End
"""
