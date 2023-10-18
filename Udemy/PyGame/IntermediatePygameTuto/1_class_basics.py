class Dog():
    """
    A class to represent a general dog
    """

    def __init__(self, name, gender, age):
        """ Initialize attributes"""
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        """ Feed the dog"""
        if self.gender == "male":
            print("Here " + self.name + "! Good Boy! Eat up.")
        else:
            print("Here :" + self.name + "! Good Girl! Eat up.")

    def bark(self, is_loud):
        """Get the dog to speak"""
        if is_loud:
            print("WOOF WOOF WOOF WOOF")
        else:
            print("woof...")

    def compute_age(self):
        """ Compute the age in dog years"""
        dog_years = self.age * 7
        print(self.name + " is " + str(dog_years) + " years old in dog years.")


# create two dogs objects from our class
dog_1 = Dog('Spot', 'male', 3)
dog_2 = Dog('Kady', 'female', 12)

# Access attribute of each individual object
print(dog_1.name)
print(dog_2.gender)
dog_1.name = "Spotty Dog"
print(dog_1.name)
print()

# Call method on the class
dog_1.eat()
dog_2.eat()
print()

dog_1.bark(True)
dog_2.bark(False)
print()

dog_1.compute_age()
dog_2.compute_age()

