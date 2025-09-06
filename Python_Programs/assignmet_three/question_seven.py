# Q7) Write program Panagram

'''
for my reference
anagram meaning :- 
A pangram is a sentence or phrase that uses every letter of a given alphabet at least once. 
In English, the most famous example is "The quick brown fox jumps over the lazy dog." 
(meaning it contains every letter of the alphabet at least once)
'''

import string # We need this to easily get all the letters of the alphabet.

sentence = 'The quick brown fox jumps over the dog'

# Make a set of all lowercase letters of the alphabet
alphabet_set = set(string.ascii_lowercase)

# Make a set of all lowercase letters found in the sentence
sentence_letters = set(sentence.lower())

# Check if the alphabet set is a subset of the sentence's letters
# This means all letters of the alphabet are present in the sentence.
if alphabet_set <= sentence_letters:
    print("The sentence is a pangram!")
else:
    print("The sentence is not a pangram.")


'''
OutPut:- 
The sentence is not a pangram.
'''
