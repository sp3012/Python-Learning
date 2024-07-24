# Problem 4: Cache Return Values (memoization)
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

def cache_return (func):
    cache = {}
    def wrapper (*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in  cache:
            print('Already present in the cache')
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        return result 
    return wrapper


@cache_return
def add (*args):
    return sum(args)


print(add(3, 6, 4, 6, 7, 10))
print(add(3, 6, 4, 6, 7, 10))