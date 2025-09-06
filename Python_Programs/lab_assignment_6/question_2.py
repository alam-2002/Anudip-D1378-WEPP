# Q2) Write a python program to check whether a number is palindrome or not?

def is_palindrome(number):
  # Convert the number to a string
  num_str = str(number)
  
  # Compare the string with its reversed version
  return num_str == num_str[::-1]

# Get input from the user
try:
  user_input = int(input("Enter a number: "))
  
  # Check and print the result
  if is_palindrome(user_input):
    print(user_input, "The number is a palindrome.")
  else:
    print(user_input, "The number is not a palindrome.")
except ValueError:
  print("Invalid input. Please enter an integer.")

'''
OutPut:- 
Enter a number: 121
121 The number is a palindrome.

Enter a number: 456
456 The number is not a palindrome.
'''
