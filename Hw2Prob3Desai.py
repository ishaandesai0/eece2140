from string import digits, ascii_lowercase
characters = digits + ascii_lowercase

def is_palindrome(word):
    word = [c for c in word.lower() if c in characters]
    return word [::-1] == word != []

check = input('Enter a word to see if it is a Palindrome: ')
print(is_palindrome(check))