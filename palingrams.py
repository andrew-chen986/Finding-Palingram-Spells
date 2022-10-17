"""Searches a list of words for two-word palingrams

Two-word palingrams are made up of a "core word" from which there is a 
"palindromic sequence" and a "reversed word" within

A semordnilap is a word that spells another different word when reversed

"""

import load_dictionary

dictionary = load_dictionary.load('2of4brif.txt')

palingrams = []

for word in dictionary:
    wordLength = len(word)
    if wordLength > 1:
        # examine from back-to-front if there is a palindromic sequence followed
        # by a reversed word
        for i in range(wordLength, -1, -1):
            # check palindromic sequence
            palindromicSequence = word[i:]
            if palindromicSequence == palindromicSequence[::-1]:
                # check if remainder of word is a reversed word
                reversedWord = word[:i]
                reversedWord = reversedWord[::-1]
                if reversedWord in dictionary:
                    print((word, reversedWord))
                    palingrams.append((word, reversedWord))

        # examine same word from front-to-back for same criteria
        for i in range(wordLength):
            # check palindromic sequence
            palindromicSequence = word[:i]
            if palindromicSequence == palindromicSequence[::-1]:
                # check if remaining word is a reversed word
                reversedWord = word[i:] 
                reversedWord = reversedWord[::-1]
                if reversedWord in dictionary:
                    print((reversedWord, word))
                    palingrams.append((reversedWord, word))
print(f"Number of two-word palingrams found: {len(palingrams)}")
print(*palingrams,sep='\n')