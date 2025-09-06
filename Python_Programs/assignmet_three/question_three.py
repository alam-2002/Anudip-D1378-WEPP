# Q3) Write program to count the number in a string


my_string = 'Anudip Foundation - 411014'

numbers = "1234567890"

count = 0

# Loop 
for num in my_string:
    # Check if the character is a digit
    if num in numbers:
        count = count + 1

# Print the total number of digits
print("Number of digits:", count)


'''
OutPut:- 
Number of digits: 6
'''
