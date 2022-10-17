"""Load a text file into a list

Arguments: path to a text file

Exceptions: IOError if text file fails to load

Returns: A list of words in the text file in lower case

"""

import sys

def load(file):
    try:
        with open(file) as dictionary:
            dictionaryList = dictionary.read().strip().split('\n')
            dictionaryList = [word.lower() for word in dictionaryList]
            return dictionaryList
    except IOError as e:
        print(f"{e}\nFailed to load file.")
        sys.exit(1)