def summarize_letters(myWord):
    wordDictionary = {}
    myWord = myWord.upper()
    myWord.split()
    wordArray = []
    for letter in myWord:
        if letter.isalpha():
            wordArray.append(letter)
            if letter not in wordDictionary:
                wordDictionary[letter] = 1
            else:
                wordDictionary[letter] += 1
    if len(set(wordDictionary)) == 26:
        print("Full alphabet present!")
    else:
        print("Full alphabet not present!")
    wordArray = [(i, n) for i, n in wordDictionary.items()]
    return tuple(wordArray), dict(wordDictionary)

print(summarize_letters('abcdefghijklmnopqrstuvwxyz'))
print(summarize_letters('Computing Fundamentals'))