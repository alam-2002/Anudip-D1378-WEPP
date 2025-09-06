# Q3) Write a python program finding the factorial of a given number using a while loop.

def findFactorialWhile(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."  #
    elif num == 0 or num == 1:
        return 1  #
    else:
        factorial = 1
        i = 1  # Initialize a counter variable
        while i <= num:  # Loop until the counter reaches the number
            factorial = factorial * i  # Multiply the factorial by the current counter value
            i = i + 1  # Increment the counter
        return factorial

# Get input from the user
try:
    number = int(input("Enter a non-negative integer: "))
    result = findFactorialWhile(number)
    print(f"The factorial of {number} is {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")



'''
OutPut:- 
Enter a non-negative integer: 5
The factorial of 5 is 120
'''
