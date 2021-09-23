# Scrable Simulator
# Erik Sundblad
# CS1030-001

import sys

word_file = open('1030 Project 04 01 Words.txt', 'r')
POINT_VALS = {}
# using dictionary.update to simplify key assignment of multiples keys to singular value
POINT_VALS.update(dict.fromkeys(['A','E','I','L','N','O','R','S','T','U'], 1))
POINT_VALS.update(dict.fromkeys(['D','G'], 2))
POINT_VALS.update(dict.fromkeys(['B','C','M','P'], 3))
POINT_VALS.update(dict.fromkeys(['F','H','V','W','Y'], 4))
POINT_VALS.update(dict.fromkeys(['K'], 5))
POINT_VALS.update(dict.fromkeys(['J','X'], 8))
POINT_VALS.update(dict.fromkeys(['Q','Z'], 10))


# function using system instruction to pipe output to text file
def print_to_file(words, scores):
    sys.stdout = open("ErikSundblad_04_01_Output.txt", 'w')
    print("Words", " " * 7, "Scores")
    print("-" * 19)
    for i in range(len(words)):
        print("{:<15} {:<4}".format(words[i], scores[i]))

    print("\nTotal", " " * 9, sum(scores))


# function to aggregate word score from point value dict
def word_score(word):
    score = 0
    if len(word) > 10 or len(word) == 0:
        return score
    for char in word:
        char = char.upper()
        if POINT_VALS.__contains__(char):
            score = score + POINT_VALS[char]
    return score


# parallel lists to hold extracted words and score
words = []
scores = []

for word in word_file:
    # test for word strips it of new line characters
    if word.rstrip():
        words.append(word.rstrip())
        scores.append(word_score(word))

# print formatted output table of words and scores
print("Words"," "*7,"Scores")
print("-"*19)
for i in range(len(words)):
    print("{:<15} {:<4}".format(words[i], scores[i]))

print("\nTotal", " "*9, sum(scores))
print_to_file(words, scores)

word_file.close()