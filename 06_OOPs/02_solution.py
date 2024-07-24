# 2. Methods in a Class

# Define a class Circle with an attribute radius.
# Include a method area that calculates the area of the circle.
# Include a method circumference that calculates the circumference of the circle.
# Create an instance of the Circle class and call the area and circumference methods.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area (self):
        circle_area = math.pi * (self.radius)**2
        return (f"Area of the circle is {circle_area:.2f}")
    
    def circumference (self):
        Circle_circum = 2 * (math.pi) * self.radius
        return (f"The circumference of the circle is {Circle_circum:.2f}")


new_circle = Circle(4)

print(new_circle.area())
print(new_circle.circumference())