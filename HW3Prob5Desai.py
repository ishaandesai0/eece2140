def securePW(password):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = '0123456789'
    characters = "!@#$%^&*<>"
    
    numUpper = 0
    numLower = 0
    numDigits = 0
    numChars = 0
    
    if len(password) >= 8 and len(password) <= 20:
        for uppercase in password:
            numUpper += 1
        for lowercase in password:
            numLower += 1
        for digits in password:
            numDigits += 1
        for characters in password:
            numChars += 1
        if(numUpper >= 1 and numLower >= 1 and numDigits >= 1 and numChars >= 1):
            print("This is a secure password")
        else:
            print("This is not a secure password")
    else:
        print("This is not a valid password")    
    
password = input("Enter a password to see if it is secure enough: ")
securePW(password)