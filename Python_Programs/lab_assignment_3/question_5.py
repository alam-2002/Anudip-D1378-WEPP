# Q5) Write a lambda function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. Test it with different numbers.

# Lambda function
check_number = lambda num: "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")

# Print it with different numbers
print("5 is = ",check_number(5)) 
print("-3 is = ",check_number(-3)) 
print("0 is = ",check_number(0))     


'''
OutPut:- 
5 is =  Positive
-3 is =  Negative
0 is =  Zero
'''
