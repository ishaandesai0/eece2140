def pigLatinGen():
    firstSentence = input("Please enter the initial phrase: \n").split()
    for x in firstSentence:
        if x[0] == "a" or x[0] == "e" or x[0] == "i" or x[0] == "o" or x[0] == "u":
            print(x[0:] + "ay", end = "")
        else:
            print(x[1:] + x[0] + "ay", end = "")
        
        print()

pigLatinGen()