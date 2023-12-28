class Dog:
    specie = 'mammal'

    def __init__(self, my_breed, name, spots):
        self.my_breed = my_breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}")


my_dog = Dog('Huskie', 'Milie', False)
my_dog.bark(56)
print(type(Dog))


class Circle:
    pi = 3.14

    def __init__(self, radius=2):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.get_circumference())
print(my_circle.radius)
print(my_circle.area)
