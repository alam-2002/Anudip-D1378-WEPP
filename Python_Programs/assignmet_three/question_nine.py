# Q9) Write program to find the number of substring


main_string = '"We will fight on the beaches. We will fight on the landing grounds. We will fight in the fields and in the streets." '

sub_string = 'We'

# Use the .count() method to count occurrences.
count = main_string.count(sub_string)

# Print the number of times the substring was found
print("The substring '", sub_string,"' appears",count,"times in the main string.")


'''
OutPut:- 
The substring ' We ' appears 3 times in the main string.
'''
