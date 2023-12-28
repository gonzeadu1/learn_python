class Animal:
    def __init__(self, legs, sleep):
        self.legs = legs
        self.sleep = sleep
        print("Animal created!")

    def who_am_I(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


# This is how to inherit in python
class Dog(Animal):
    specie = 'mammal'

    def __init__(self, my_breed, name, spots, legs, sleep):
        super().__init__(legs, sleep)
        print("Dog Created")
        self.my_breed = my_breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}")

    def who_am_I(self):
        print("I am a dog!")

    def eat(self):
        print("I am eating and eating")


my_dog = Dog('Huskie', 'Sammy', True, False, True)

print(my_dog.__init__('Huskie', 'Sammy', True, False, True))

my_dog.who_am_I()
my_dog.eat()

print(
    "==================================================================================================================================")


# polymorphism
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says Woof, woff!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says Meow, Meow!"


niko = Dog("niko ")
print(niko.speak())

felix = Cat("felix ")
print(felix.speak())

# example 1 of how to use polymorphism
print(
    "==================================Using Loops to explain polymorphism=======================================")
for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

print(
    "===========================Using functions to explain polymorphism==========================================")


# example 2 of how to use polymorphism
def pet_speak(self):
    print(self.speak())


print(pet_speak(felix))
print(pet_speak(niko))

print("===========Using Abstract Classes to Explain Polymorphism===============================")


# example 3 of how to use polymorphism
class Animal3:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog3(Animal3):
    def speak(self):
        return self.name + " says woof!"


class Cat3(Animal3):
    def speak(self):
        return self.name + " says meow!"


fido = Dog3("fido")
print(fido.speak())
isis = Cat3("isis")
print(isis.speak())

print("===============================Special Methods===============================")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Remember toStrings() method
    def __str__(self):
        return f"{self.title} written by {self.author}"

    def __del__(self):
        print(f"{self.title} has been deleted")

    def __len__(self):
        return self.pages


my_book = Book("Basics of Python", "Gideon Nzeadu", 200)
print(my_book)
print(my_book.__len__())
del my_book