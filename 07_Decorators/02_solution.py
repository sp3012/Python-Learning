# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time

def time_calculator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken to execute the function {func.__name__}  is {time_taken:.4f} seconds")
        return result
    return wrapper

@time_calculator
def add(a, b):
    time.sleep(4)
    return a + b
print(add(2, 3))

# __name__ it is used to show the name of the function. 