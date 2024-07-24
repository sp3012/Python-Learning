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
print(my_triangle.area())