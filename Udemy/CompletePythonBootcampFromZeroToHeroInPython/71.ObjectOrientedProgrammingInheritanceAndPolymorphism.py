"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478298#search
Object Oriented Programming Part Three
"""

# class Animal():
#     def __init__(self):
#         print("ANIMAL CREATED")
#
#     def who_am_i(self):
#         print("I am an animal")
#
#     def eat(self):
#         print("I am eating")
#
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")
#
#     def who_am_i(self):
#         print("I am a dog!")
#
#     def bark(self):
#         print("WOOF!")
#
#     def eat(self):
#         print("I am a dog and eating")
#
#
# mydog = Dog()
# mydog.eat()
#
# mydog.who_am_i()
# mydog.bark()

# ---------------
# Polymorphisme -
# ---------------
# class Dog():
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + "Says woof!"
#
#
# class Cat():
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + "says meow!"
#
#
# niko = Dog("niko")
# felix = Cat("felix")
#
# print(niko.speak())
# print(felix.speak())
#
# for pet in [niko, felix]:
#     print(type(pet))
#     print(pet.speak())
#
#
# def pet_speak(pet):
#     print(pet.speak())
#
#
# pet_speak(niko)
# pet_speak(felix)

# A more common practice is to use abstract classes and inheritance
# An abstract classes is a class that never expect to be instanciated. It only serves as a base class.

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


myanimal = Animal('fred')


class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"


fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())