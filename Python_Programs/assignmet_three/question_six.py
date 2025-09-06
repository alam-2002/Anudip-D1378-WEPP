# Q6) Write program anagram

'''
for my reference
anagram meaning :- 
An anagram is a word or phrase that's formed by rearranging the letters of another word or phrase. 
For example, the letters that make up “A decimal point” can be turned into the anagram “I’m a dot in place.” 
(meaning they contain the same letters, but in a different order)
'''

string1 = 'Listen'
string2 = 'Silent'

# Convert both strings to lowercase and sort them for compare the letters
sorted_string1 = sorted(string1.lower())
sorted_string2 = sorted(string2.lower())

# Check if the sorted lists of characters are the same
if sorted_string1 == sorted_string2:
    print("The strings are anagrams!")
else:
    print("The strings are not anagrams.")


'''
OutPut:- 
The strings are anagrams!
'''
