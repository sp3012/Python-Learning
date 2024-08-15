<<<<<<< HEAD
# Polymorphism

# Define a base class Shape with a method area.
# Create two subclasses Rectangle and Triangle that inherit from Shape and implement the area method.
# Create instances of Rectangle and Triangle and call their area methods.

class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area (self):
        pass

class Rectangle(Shape):
    def area(self):
        return self.height * self.base
    
class Triangle (Shape):
    def area(self):
        return (0.5 * (self.height * self.base))
    
my_rectangle = Rectangle(2, 3)
my_triangle = Triangle(2, 3)

print(my_rectangle.area())
=======
# Polymorphism

# Define a base class Shape with a method area.
# Create two subclasses Rectangle and Triangle that inherit from Shape and implement the area method.
# Create instances of Rectangle and Triangle and call their area methods.

class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area (self):
        pass

class Rectangle(Shape):
    def area(self):
        return self.height * self.base
    
class Triangle (Shape):
    def area(self):
        return (0.5 * (self.height * self.base))
    
my_rectangle = Rectangle(2, 3)
my_triangle = Triangle(2, 3)

print(my_rectangle.area())
>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
print(my_triangle.area())