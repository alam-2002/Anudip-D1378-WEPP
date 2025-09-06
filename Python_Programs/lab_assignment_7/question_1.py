# -------------------- Experiment 1:  7 Lab-Python-Advance-05-SEPT-2025 --------------------

# Q1) Write a decorator that ensures that all input arguments to a function are non-negative integers.

def non_negative_integers_only(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance(arg, int) or arg < 0:
                raise ValueError("All arguments must be non-negative integers")
        return func(*args, **kwargs)
    return wrapper


@non_negative_integers_only
def add(a, b):
    return a + b


# Example:
print(add(5, 10))   # Works
# print(add(-1, 3))  # Raises ValueError



'''
OutPut:- 
15
'''
