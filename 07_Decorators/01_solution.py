<<<<<<< HEAD
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

=======
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
add(5, 3)