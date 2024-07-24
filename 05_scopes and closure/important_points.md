1. What is a closure in Python?
    A closure in Python is a function object that has access to variables in its lexical scope, even when the function is called outside that scope. Closures are created when a nested function captures the local variables from its enclosing function.

2. How do you create a closure in Python?
    A closure is created by defining a nested function inside an enclosing function and then returning the nested function. The nested function can access the variables of the enclosing function.

3. What are the use cases of closures in Python?
    Closures can be used for data hiding, maintaining state between function calls, creating function factories, and callback functions.

4. What is the difference between a closure and a regular function?
     A regular function only has access to its own local variables and global variables. A closure, however, has access to its own local variables, global variables, and variables from its enclosing scope, even after the enclosing function has finished executing.

5. Can you modify the variables captured by a closure?
    Yes, you can modify the variables captured by a closure using the 'nonlocal' keyword if the variable is from an enclosing non-global scope.

    EX. 
    def outer_function(msg):
        def inner_function():
            nonlocal msg
            msg = "Modified message"
            print(msg)
        inner_function()
        print(msg)

    outer_function("Original message")
    # Output:
    # Modified message
    # Modified message

6. How can you prevent variables in a closure from being modified?
    To prevent variables in a closure from being modified, you can avoid using the nonlocal keyword and ensure that the variables are not reassigned within the inner function.

7. What are some common pitfalls when working with closures?
    Common pitfalls include:
        Unintended sharing of state between different instances of closures.
        Modifying enclosed variables unintentionally.
        Confusion between global, local, and nonlocal scopes.


----    Both closures and generators are powerful tools in Python, and choosing between them depends on the specific requirements of your task. For maintaining state across function calls with encapsulation, closures are typically more suitable. For generating sequences of values efficiently with lazy evaluation, generators are the better choice.


****************** SCOPE **************************

1. What are the different types of scopes in Python?
    The different types of scopes in Python are:
        Local Scope: Variables defined inside a function.
        Enclosing Scope: Variables in the local scope of enclosing functions (nested functions).
        Global Scope: Variables defined at the top level of a script or module.
        Built-in Scope: Names preassigned in Python, such as keywords and functions like len, int, etc.

        LEGB stands for Local, Enclosing, Global, and Built-in. It is the rule Python uses to resolve the scope of a variable. It looks for a variable in this order: first in the local scope, then in the enclosing scope, followed by the global scope, and finally in the built-in scope.

2. What is the difference between global and nonlocal keywords?
    The global keyword is used to declare that a variable inside a function is global.
    The nonlocal keyword is used to declare that a variable inside a nested function is not local to that function, but it is from an enclosing scope.
    python

3. How can you access a global variable inside a function without using the global keyword?
    You can access (but not modify) a global variable inside a function without using the global keyword.

4. 