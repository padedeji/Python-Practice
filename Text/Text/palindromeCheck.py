# Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar.”

def palindromeCheck():
    text = raw_input("Please enter a palindrome. ")
    if text[::-1] == text:
        return "This is a palindrome."
    else:
        return "This is not a palindrome."

print(palindromeCheck())
