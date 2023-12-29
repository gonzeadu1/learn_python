import math


class Line:

    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        (x1, y1) = self.coordinate1
        (x2, y2) = self.coordinate2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def __str__(self):
        return f"The two coordinates are {self.coordinate1} and {self.coordinate2}"

    def slope(self):
        (x1, y1) = self.coordinate1
        (x2, y2) = self.coordinate2
        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li)
print("The distance between the two coordinates are:", round(li.distance(), 3))
print("The slope size is:", li.slope())


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def __str__(self):
        return f"The height is {self.height} and the radius is {self.radius}"

    def volume(self):
        return self.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        lateral_area = 2 * self.pi * self.radius * self.height
        end_area = 2 * self.pi * self.radius ** 2
        return lateral_area + end_area


cylinder = Cylinder(2, 3)
print(cylinder)
print("The volume of the cylinder is: ", cylinder.volume())
print("The surface area of the cylinder is: ", cylinder.surface_area())
