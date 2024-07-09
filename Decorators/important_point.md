1. What are Decorators?
    Decorators in Python are a powerful tool that allows you to modify the behavior of a function or method. They enable you to wrap another function to extend its behavior without permanently modifying it. This is especially useful for cross-cutting concerns like logging, access control, and instrumentation.

    They are particularly useful for implementing cross-cutting concerns in a DRY (Don't Repeat Yourself) manner.

2. How Decorators Work
    A decorator is essentially a higher-order function that takes another function as an argument and returns a new function that usually extends the behavior of the original function.