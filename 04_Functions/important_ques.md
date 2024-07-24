1. What is a function in Python, and why are they used?
    A function in Python is a block of reusable code that performs a specific task or a set of tasks. Functions help in organizing and managing code efficiently, promoting code reusability and modularity.

2. What is the difference between a function and a method in Python?
    Functions are independent blocks of code that perform tasks and can be called directly.
    Methods are functions that belong to objects and are defined within classes, with the first parameter typically being self to access instance attributes.

3. Can you explain the difference between arguments and parameters in a function?
    Parameters are placeholders defined in the function signature to indicate what inputs the function expects.
    Arguments are the actual values passed to the function when it is called.

4. What are default arguments in a function? Give an example.
    Default arguments in a function allow you to provide default values for some parameters, making them optional during the function call. If an argument for an optional parameter is not provided, the default value is used. This feature adds flexibility, simplicity, and readability to function definitions and calls in Python.

5. Explain what keyword arguments are in Python functions.
    Keyword arguments in Python functions allow you to pass arguments using the parameter names explicitly, making function calls more readable and flexible. They help improve code readability, reduce errors, and provide flexibility in the order of arguments. Keyword arguments can be combined with positional arguments, with positional arguments appearing before keyword arguments.

6. What are arbitrary arguments (*args) and keyword arguments (**kwargs)? How are they used?
*args:
    Used to pass a variable number of positional arguments.
    Collected as a tuple.
    Syntax: *args.

**kwargs:
    Used to pass a variable number of keyword arguments.
    Collected as a dictionary.
    Syntax: **kwargs.

7. What is the difference between positional and keyword arguments?
Positional Arguments:
    Passed in a specific order.
    Order matters.
    Less readable if there are many arguments.

Keyword Arguments:
    Passed by explicitly naming the parameters.
    Order does not matter.
    More readable and flexible.
    Useful for overriding default parameter values.

8. How does the return statement work in a Python function?
Purpose: The return statement is used to exit a function and pass back a value to the caller.
Behavior:
    Stops function execution and returns control to the caller.
    Can return a single value, multiple values (as a tuple), or None (if no value is specified).
Syntax: return expression or simply return for returning None.
Examples: Returning single/multiple values, returning None by default, and conditional return statements.

9. What are lambda functions in Python? Provide an example.
    Lambda functions, also known as anonymous functions, are small, single-expression functions that are defined using the lambda keyword. They are useful when you need a simple function that is short and temporary.

    Syntax
    lambda arguments: expression

10. What are some common use cases for lambda functions?
    Lambda functions are often used with functions like map(), filter(), and reduce() for simple data transformations and processing.

### ### ### Generators:

11. What are generator functions in Python?
     Generator functions in Python are functions that enable the creation of iterators using the yield keyword. They allow you to define an iterative algorithm by writing a single function that can maintain its state across multiple calls. Generator functions produce values one at a time and only when requested, which makes them memory efficient and suitable for handling large datasets or infinite sequences.

12. How do generators differ from regular functions?
    regular functions and generator functions differ in their execution model, handling of state, return mechanism, memory usage, and suitability for different programming scenarios. Regular functions are used for general computation and immediate result return, while generator functions excel in producing sequences lazily, maintaining state, and optimizing memory usage, especially for large datasets or infinite sequences. Understanding these differences helps in choosing the appropriate function type based on the specific requirements of your programming task.

13. Explain how the yield keyword works.
    The yield keyword in Python is used in generator functions to produce a sequence of values lazily, one at a time, instead of computing and returning all values at once. It enables the creation of iterators with minimal overhead and facilitates efficient handling of large datasets or infinite sequences.

Execution Flow
    First Call: When a generator function is called, it returns a generator object without executing the function's body immediately.

    Iterator Protocol: The generator object follows the iterator protocol, implementing __iter__() and __next__() methods automatically. These methods manage the execution of the generator function.

    Iteration: Each time the next() function is called on the generator object or it is used in a for loop, the function's execution progresses until a yield statement is encountered.

    Yielding Values: When yield is encountered, the current state of the function is frozen, and the yielded value is returned to the caller. The function is paused but retains its local variables and execution state.

    Resuming Execution: Upon the next iteration or call to next(), the function resumes execution immediately after the yield statement, continuing until the next yield or return statement is encountered.

14. What are the advantages of using generators?
    Generators in Python provide a versatile and efficient mechanism for generating sequences lazily, optimizing memory usage, and facilitating iterative and stream processing. They improve code readability, simplify complex computations, and enable handling of large datasets or continuous data streams with minimal overhead. 



####
LEFT TOPICS IN FUNCTIONS

Scope and Lifetime:
Higher-Order Functions
Decorators
Function Annotations
Error Handling