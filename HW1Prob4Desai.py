from random import randint

randomNumber = randint(1,1000)

while True:
    userGuess = int(input("Enter a number between 1 and 1000: "))
    if userGuess > randomNumber:
        print("Too high. Try again. ")
    elif userGuess < randomNumber:
        print("Too low. Try again.")
    else:
        print("Congratulations.  You guessed the number!")
        choice = input("Would you like to play again? (y/n): ")
        if choice == 'n':
            break    
    
var1 = [k**2 for k in range(5)]
var2 = tuple([-k for k in range (4)])
