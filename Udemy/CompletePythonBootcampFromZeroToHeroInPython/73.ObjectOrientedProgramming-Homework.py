"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478312#search
Object Oriented Programming Homework Overview
"""
# Problem 1
from math import sqrt, pi


class Line:
    def __init__(self, coor1, coor2):
        self.coor1x, self.coor1y = coor1
        self.coor2x, self.coor2y = coor2

    def distance(self):
        """
        distance = sqrt((x2-x1)**2 + (y2 - y1)**2)
        slope = (y2 -y1)/(x2 -x1)
        """
        return sqrt((self.coor2x - self.coor1x) ** 2 + (self.coor2y - self.coor1y) ** 2)

    def slope(self):
        return (self.coor2y - self.coor1y) / (self.coor2x - self.coor1x)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


# # Problem 2
class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * pi * self.radius ** 2

    def surface_area(self):
        top = 3.14 * (self.radius**2)
        return (2*top) + (2*pi*self.radius*self.height)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
