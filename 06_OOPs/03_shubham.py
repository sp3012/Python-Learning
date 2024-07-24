# Inheritance

# Create a base class Animal with attributes name and species.
# Define a method make_sound that prints a generic sound.
# Create a subclass Dog that inherits from Animal and overrides the make_sound method to print "Bark".
# Create an instance of the Dog class and call the make_sound method.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        return "Generic sound"

class Dog(Animal):
    def make_sound (self):
        return "Bark"
    
dog = Dog("Sunny", "Labra")

print(dog.make_sound())