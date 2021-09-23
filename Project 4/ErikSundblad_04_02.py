# Letter Frequency Counter
# Erik Sundblad
# CS1030-001

import sys

in_file = open("1030 Project 04 02 Sentences.txt", 'r')

# Using update to create all keys and instantiate them with the value 0
alphabet = {}
alphabet.update(dict.fromkeys(['A','B','C','D','E','F','G','H','I','J','K','L','M',
                               'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], 0))


# function using system instruction to pipe output to text file
def print_to_file(dict):
    sys.stdout = open("ErikSundblad_04_02_Output.txt", 'w')
    print("Letter   Frequency\n" + "-" * 20)
    for keys in alphabet:
        print(" ", keys, " " * 7, alphabet[keys])
alphabet.__setitem__()

# nested for loops to extract words from file then extract chars from word and increment found chars in alpha
for words in in_file:
    if words:
        for char in words:
            if char:
                if alphabet.__contains__(char.upper()):
                    alphabet[char.upper()] += 1

# Print header then using for loop print key/value pairs in column formation
print("Letter   Frequency\n" + "-"*20)
for keys in alphabet:
    print(" ", keys, " "*7, alphabet[keys])
print_to_file(alphabet)

in_file.close()
