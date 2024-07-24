1. What are Decorators?
    Decorators in Python are a powerful tool that allows you to modify the behavior of a function or method. They enable you to wrap another function to extend its behavior without permanently modifying it. This is especially useful for cross-cutting concerns like logging, access control, and instrumentation.

    They are particularly useful for implementing cross-cutting concerns in a DRY (Don't Repeat Yourself) manner.

2. How Decorators Work
    A decorator is essentially a higher-order function that takes another function as an argument and returns a new function that usually extends the behavior of the original function.

3. How do you apply a decorator to a function?
    Applying a decorator to a function in Python is straightforward. You can use the @decorator_name syntax above the function definition.

4. What is the purpose of the *args and **kwargs in a decorator?
    The *args and **kwargs in a decorator are used to allow the decorator to accept any number of positional and keyword arguments when it wraps a function. This ensures that the decorator can be applied to a wide variety of functions with different signatures without modifying the decorator code for each specific function.

5. Can a decorator be used with a class method? If so, how?
    Yes, decorators can be used with class methods in Python. Decorators can be applied to class methods in the same way they are applied to regular functions.

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Calling method {func.__name__}")
            result = func(*args, **kwargs)
            print(f"Method {func.__name__} finished")
            return result
        return wrapper

    class MyClass:
        @my_decorator
        def my_method(self, x, y):
            print(f"MyClass.my_method called with {x} and {y}")
            return x + y

    # Create an instance of MyClass
    obj = MyClass()

    # Call the decorated method
    result = obj.my_method(10, 20)
    print("Result:", result)

    OUTPUT
    Calling method my_method
    MyClass.my_method called with 10 and 20
    Method my_method finished
    Result: 30


6. What are some common use cases for decorators?
        Logging
        Timing
        Authorization
        Memoization/Caching
        Input validation
        Access control
        Rate limiting
        Tracing
        Exception handling
        Resource management (e.g., opening and closing files or network connections)