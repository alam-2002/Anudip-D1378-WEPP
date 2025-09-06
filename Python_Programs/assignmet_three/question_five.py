# Q5) Write program to find "a" character in the String


my_string = 'Hello, Myself Alam'

# Find the first 'a' in string
position = my_string.find("a")

# find 'a'
if position != -1:
    print("The character 'a' is found at index:", position)
else:
    print("The character 'a' is not found in the string.")



'''
OutPut:- 
The character 'a' is found at index: 16
'''
