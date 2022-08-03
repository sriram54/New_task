"""
In this code I have plotted 2 random points A and Bin 3D space then
it will divide it to 6 parts and plot 5 equidistant points between them,
Then, it gives the co-ordinates of point A and B

The shortest distance travelled between two points is Given after running the code
Cylinder will be plotted in next part .
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

ax = plt.axes(projection='3d')
ax.set_xlabel(r'X')
ax.set_ylabel(r'Y')
ax.set_zlabel(r'Z')
ax.set_title('Two 3D Points in Space')


class Points:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Solution for tranversing from point A to Point B
    def distance(self):
        print(f'starting point A: {[self.x[0], self.y[0], self.z[0]]}')
        print(f'ending point B: {[self.x[1], self.y[1], self.z[1]]}')
        d = sqrt((self.x[1] - self.x[0]) ** 2 +
                 (self.y[1] - self.y[0]) ** 2 +
                 (self.z[1] - self.z[0]) ** 2)
        return d

    def midpoint(self):
        m = [((self.x[1] + self.x[0]) / 2),
             ((self.y[1] + self.y[0]) / 2),
             ((self.z[1] + self.z[0]) / 2)]
        return m

    # For getting five equidistant points b/w Two points A and B
    def five_equidistant_point(self):
        p1 = [(self.x[0] + ((self.x[1] - self.x[0]) * (1 / 6))),
              (self.y[0] + ((self.y[1] - self.y[0]) * (1 / 6))),
              (self.z[0] + ((self.z[1] - self.z[0]) * (1 / 6)))]

        p2 = [(self.x[0] + ((self.x[1] - self.x[0]) * (2 / 6))),
              (self.y[0] + ((self.y[1] - self.y[0]) * (2 / 6))),
              (self.z[0] + ((self.z[1] - self.z[0]) * (2 / 6)))]

        p3 = [(self.x[0] + ((self.x[1] - self.x[0]) * (3 / 6))),
              (self.y[0] + ((self.y[1] - self.y[0]) * (3 / 6))),
              (self.z[0] + ((self.z[1] - self.z[0]) * (3 / 6)))]

        p4 = [(self.x[0] + ((self.x[1] - self.x[0]) * (4 / 6))),
              (self.y[0] + ((self.y[1] - self.y[0]) * (4 / 6))),
              (self.z[0] + ((self.z[1] - self.z[0]) * (4 / 6)))]

        p5 = [(self.x[0] + ((self.x[1] - self.x[0]) * (5 / 6))),
              (self.y[0] + ((self.y[1] - self.y[0]) * (5 / 6))),
              (self.z[0] + ((self.z[1] - self.z[0]) * (5 / 6)))]

        return p1, p2, p3, p4, p5


x_data = np.random.randint(0, 10, (2))
y_data = np.random.randint(0, 10, (2))
z_data = np.random.randint(0, 10, (2))

x_list = x_data
y_list = y_data
z_list = z_data

jkl = Points(x_list, y_list, z_list)
print(f'The shortest distance between two points is {jkl.distance()}')
print(f'The five equidistant points are:\n\t{jkl.five_equidistant_point()}')

ax.scatter((x_list[0] + ((x_list[1] - x_list[0]) * (1 / 6))),
           (y_list[0] + ((y_list[1] - y_list[0]) * (1 / 6))),
           (z_list[0] + ((z_list[1] - z_list[0]) * (1 / 6))))

ax.scatter((x_list[0] + ((x_list[1] - x_list[0]) * (2 / 6))),
           (y_list[0] + ((y_list[1] - y_list[0]) * (2 / 6))),
           (z_list[0] + ((z_list[1] - z_list[0]) * (2 / 6))))

ax.scatter((x_list[0] + ((x_list[1] - x_list[0]) * (3 / 6))),
           (y_list[0] + ((y_list[1] - y_list[0]) * (3 / 6))),
           (z_list[0] + ((z_list[1] - z_list[0]) * (3 / 6))))

ax.scatter((x_list[0] + ((x_list[1] - x_list[0]) * (3 / 6))),
           (y_list[0] + ((y_list[1] - y_list[0]) * (3 / 6))),
           (z_list[0] + ((z_list[1] - z_list[0]) * (3 / 6))))

ax.scatter((x_list[0] + ((x_list[1] - x_list[0]) * (4 / 6))),
           (y_list[0] + ((y_list[1] - y_list[0]) * (4 / 6))),
           (z_list[0] + ((z_list[1] - z_list[0]) * (4 / 6))))

ax.scatter((x_list[0] + ((x_list[1] - x_list[0]) * (5 / 6))),
           (y_list[0] + ((y_list[1] - y_list[0]) * (5 / 6))),
           (z_list[0] + ((z_list[1] - z_list[0]) * (5 / 6))))

ax.scatter(x_list, y_list, z_list)
ax.plot(x_list, y_list, z_list)
plt.show()
