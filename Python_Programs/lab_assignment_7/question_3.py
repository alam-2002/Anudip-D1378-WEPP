# Q3) Write a decorator that repeats the execution of a function a specified number of times

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                print(f"Execution {i+1}/{n}")
                result = func(*args, **kwargs)
            return result  # Return last result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


# Example:
greet("Alam")


'''
OutPut:- 
Execution 1/3
Hello, Alam!
Execution 2/3
Hello, Alam!
Execution 3/3
Hello, Alam!
'''
