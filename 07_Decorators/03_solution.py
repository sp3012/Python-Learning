# Problem 3: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


def debugger (func):
    def wrapper (*args, **kwargs):
        print(f" The name of the function is {func.__name__}, and the arguments passed to this function are: {args} and keywaord arguments are: {kwargs}")
        result  = func(*args, **kwargs)
   
        return result
    return wrapper

@debugger
def multiply (a, b, c):
    return a*b*c

multiply(2, 5, 4)