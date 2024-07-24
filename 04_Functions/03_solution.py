# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply (a, b):
    return a*b
result = multiply("s", 2)
result = multiply(2, 's')
result = multiply(2, 'shubham')
print(result)