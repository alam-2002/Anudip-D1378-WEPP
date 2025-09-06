# -------------------- Experiment 1:  6 Lab-Python-Core-22-AUG-2025 --------------------

# Q1) Write a python program to reverse a number using a while loop. 

num = 987654321

reversed_num = 0

# While loop 
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

# Print the reversed number
print("Reversed number:", reversed_num)


'''
OutPut:- 
Reversed number: 123456789
'''
