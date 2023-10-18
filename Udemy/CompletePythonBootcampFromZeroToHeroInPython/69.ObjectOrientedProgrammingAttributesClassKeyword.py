"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478292#search
Object Oriented Programming Part One
"""


class Dog():

    def __init__(self, breed: str, name: str, spots: bool):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots


my_dog = Dog(breed='lab', name='Sammy', spots=False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
