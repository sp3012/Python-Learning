# Static Methods

# Define a class MathOperations with a static method add that takes two numbers and returns their sum.
# Call the static method without creating an instance of the class.

class MathOperations:
    
    @staticmethod
    def add (num1, num2):
        return num1 + num2
    
print(MathOperations.add(2, 3))