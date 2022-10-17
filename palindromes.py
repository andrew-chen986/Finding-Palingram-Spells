"""Searches a list of words for palindromes"""

import load_dictionary

file = '2of4brif.txt'
dictionary = load_dictionary.load(file)
palindromes = []
for word in dictionary:
    if word == word[::-1]:
        palindromes.append(word)
print(f"Number of palindromes found: {len(palindromes)}")
print(*palindromes, sep='\n')