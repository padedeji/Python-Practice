# Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

def count_vowels():
    text = raw_input("Give me some text. ")
    textList = list(text)
    count = 0
    for letter in textList:
        if letter in "aeiou":
            count +=1
    return "There are %.i vowels in '%s.'" % (count, text)

print(count_vowels())
