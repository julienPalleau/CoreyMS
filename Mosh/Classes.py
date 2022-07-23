#############################
# DRY Don't Repeat Yourself #
#############################


print("\n Creating Classes")
############################
class Point:
    def draw(self):
        print("draw")

point = Point()
print(type(point))
print(isinstance(point, Point))

print("\n Constructors")
########################
class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point2 ({self.x}, {self.y})")


print("\n Class vs Instance Attributes")
##########################################
class Point3:
    default_color = "red" # class level attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point3 ({self.x}, {self.y})")

point = Point2(1, 2)
point.draw()

another = Point3(3, 4)
print(another.default_color) # here we ask to the object and to the instance of a class.
# Class level attributes are shared across all the classes

print(Point3.default_color) # here we ask to the class
another.draw()

print("\n Class vs Instance Methods")
#####################################
class Point4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls): # class method
        return cls(0, 0)

    def draw(self):
        print(f"Point4 ({self.x}, {self.y})")

point = Point4.zero()
point.draw()

print("")


class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets_crees = 0  # Le compteur vaut 0 au départ

    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1

    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(
            cls.objets_crees))

    combien = classmethod(combien)

Compteur.combien()
a = Compteur()
Compteur.combien()
b = Compteur()
Compteur.combien()

print("\n Magic Methods")
#########################
class Point5:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point5 ({self.x}, {self.y})")

point = Point5(1, 2)
print(str(point))

print("\n Comparing Objects")
#############################
class Point6:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

point = Point6(10, 20)
other = Point6(1, 2)
print(point == other)
print(point > other)
print(point < other)

print("\n Performing arithmetic Operations between two objects")
################################################################
class Point7:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point7(self.x + other.x, self.y + other.y)

point = Point7(10, 20)
other = Point7(1, 2)
combined = point + other
print(combined.x, combined.y)

print("\n Making custom containers")
####################################
class TagCloud:
    def __init__(self):
        self.__tags = {} # when you prefix an attribute with __ like __tags it is considered as private attribute

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

# why are we not using a classical dictionary? Because a dictionary can't deal with Python and python,
# they will make distinct count when we want one. So we can make our custom containers smarter than a
# simple dictionary

cloud = TagCloud()
# cloud(cloud.__tags)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud["Python"])
# print(cloud.__tags["PYTHON]"])

print("\n Properties")
######################
class Product:
    def __init__(self, price):
        self.price = price

# with this Product class we can create an object with negative price:
product = Product(-50)

# so how to proceed to stop negative prices
# 2 solutions:
# 1 - non pythonic solution
# class Product1:
#     def __init__(self, price):
#         self.set_price(price)
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("- Price cannot be negative.")
#         self.__price = value
#
# product1 = Product1(-50)


# # 2 - pythonic solution using properties
# class Product2:
#     def __init__(self, price):
#         self.price = price
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("- Price cannot be negative.")
#         else:
#             self.__price = value
#
#
#
# product2 = Product2(10)
# product2.price = -1
# print(product2.price)
# # A propertie is an object that seats in front of an attribute and allow us to set or get the value of an attribut

print("\n Inheritance")
#######################
# class Animal:
#     def __init__(self):
#         self.age = 1
#
#     def eat(self):
#         print("eat")
#
# # Animal: Parent, Base
# # Mammal: Child, Sub
# class Mammal(Animal):
#     def walk(self):
#         print("walk")
#
# class Fish(Animal):
#     def swim(self):
#         print("swim")
#
# m = Mammal()
# m.eat()
# print(m.age)

# print("\n The Object Class")
# ############################
# print(isinstance(m, Mammal))
# print(issubclass(Mammal, Animal))

print("\n Method Overriding")
#############################
# Method overriding means extending or replacing a method defined in the base class
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def __init__(self): # method overriding
        super().__init__() # use the init from Animal class
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
print(m.age)
print(m.weight)

print("\n Multi-level Inheritance")
###################################
# limit the multi-level to one or two beyond that it is too much complexity and you shoot yourself in the foot

print("\n Multiple inheritance")
################################
# like for multi level with multiple inheritance you have to be extra cautious.
# Multiple inheritance is a good thing as long as classe have nothing in common unlike below with greet method.

class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet() # it calls employee Greet as Employee class is called first

# here is a good example of multiple inheritance
class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass

print("\n A good example of inheritance")
#########################################
# class InvalidOperationError(Exception):
#     pass
#
# class Stream:
#     def __init__(self):
#         self.opened = False
#
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open")
#         self.opened = True
#
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already close")
#         self.opened = False
#
# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")
#
# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

print("\n Abstract Base Classes")
#################################
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")

stream = MemoryStream()
stream = Stream()
stream.open()