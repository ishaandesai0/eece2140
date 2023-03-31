from itertools import permutations

word = input("Please enter a word with 5 letters: ")
if (len(word) == 5):
    values = list(permutations(word, 3))
    for x in range(len(values)):
        string1 = ""
        print (string1.join(values[x]))
else:
    print ("Word isn't 5 letters, try again")