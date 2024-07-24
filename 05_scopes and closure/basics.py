

# ********* CLOSURE **********

# Example of factory function

def outer_func (num):
    def main (x):
        return x ** num
    return main

square = outer_func(2)
cube = outer_func(3)

print(square)
print(cube)

# humne kya kiya ki ander wale function ko return kr dya lekin bahar wale function k return me ander wale function ka only refrence dya hai humne uske execute nahi kiya. To kuki square = outer_func(2) hai to square me to wahi store hoga jo outer_func(2) ko run krne k baad aaega. lekin ye to kuch return kr hi nahi raha h ye to khali refrence lye baitha h andr wale function ka, to ye us function (ander wale) function ko hi lye baitha hai.
# isliye ab hume square ko bhi execute karana hoga.

print(square(2))
print(cube(2))

# ab ye 2 ka square nikal ra h or 2 ka cube nikal ra h. isiko closure bolte h. hume square ko bhi execute karana hota h. 
# to ab jb ander wale function ko call kr rahe hai to wo bahar wale function k variable ka bhi access le leta h(un variables ka jo ander wale me use ho rahe hai). isi ko closure bolte hai.

# square = outer_func(2) creates a function that squares a number.
# cube = outer_func(3) creates a function that cubes a number.
# The square and cube functions can then be used independently to perform their respective operations.

# ye example hume function ki factory bana k dera h, matlb outer_func me alag alag argument pass kr kr k hum square, cube, 4 , 5, 6, etc na jane kitne function bana sakte hai. 
# or fir is function ko call krke kisi bhi number ka square ya cube nikal sakte h.







# 2. how closures can be used to maintain state between function calls.

def make_counter():
    count = 0  # This variable will be captured by the closure
    
    def counter():
        nonlocal count  # Use the 'nonlocal' keyword to modify the captured variable
        count += 1
        return count
    
    return counter

# Create an instance of the counter
counter1 = make_counter()

# Use the counter
print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter1())  # Output: 3

# Create another instance of the counter
counter2 = make_counter()
print(counter2())  # Output: 1
print(counter2())  # Output: 2

# The counter function captures the count variable from its enclosing scope (make_counter). This captured variable persists between calls to counter.
# Each time the counter function is called, it updates the count variable. Since count is part of the closure, its value is retained across function calls.
# The nonlocal keyword is used inside the counter function to indicate that count is not a local variable to counter, but is from the enclosing scope (make_counter). This allows counter to modify count.
# By calling make_counter multiple times, you can create multiple independent instances of the counter function, each with its own count variable.

# Practical Use Cases
#   Callbacks and Event Handlers: Closures can maintain state information between events.
#   Function Factories: Generate customized functions with preserved state.
#   Decorators: Maintain state information in a decorator without using global or instance variables.




