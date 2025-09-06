# Q2) Write a decorator that prints out the function’s name, arguments, and return value every time it is called. This can help debug and trace the execution of the function.

def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper


@debug_decorator
def multiply(x, y):
    return x * y


# Example:
multiply(4, 5)


'''
OutPut:- 
Calling function: multiply
Arguments: args=(4, 5), kwargs={}
Return value: 20
'''
