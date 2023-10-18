import math


class Line():
    def __init__(self, coor1, coor2):
        self.coor1x, self.coor1y = coor1
        self.coor2x, self.coor2y = coor2

    def distance(self):
        return math.sqrt((self.coor2x - self.coor1x)**2 + (self.coor2y - self.coor1y)**2)

    def slope(self):
        return (self.coor2y - self.coor1y)/(self.coor2x - self.coor1x)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(f"la distance est {li.distance():10.2f}")
print(f"la pente est {li.slope():10.2f}")


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (math.pi * self.radius**2 * self.height)

    def surface_area(self):
        return (2 * math.pi * self.radius * (self.height + self.radius))


c = Cylinder(2, 3)
print(f"le volume est {c.volume():10.2f}")
print(f"la surface est {c.surface_area():10.1f}")
