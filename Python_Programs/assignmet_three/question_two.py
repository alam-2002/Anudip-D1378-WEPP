# Q2) Write program to count the Vowels in the String


my_string = 'Alamgir Mulla'

# List of vowels
vowels = "aeiouAEIOU"

# Start a counter for vowels
vowel_count = 0

# Loop 
for char in my_string:
    # Check if the character is a vowel
    if char in vowels:
        vowel_count = vowel_count + 1

# Print the total number of vowels
print("Number of vowels:", vowel_count)


'''
OutPut:- 
Number of vowels: 5
'''
