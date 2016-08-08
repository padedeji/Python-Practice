# Enter a string and the program will reverse it and print it out.
# Herein lies two different ways to do this.

def reverse_string_easy(text):
    return text[::-1]

def reverse_string(text):
    reverse = ""
    for i in range(len(text)):
        reverse += text[len(text)-i-1] # Just here
    return reverse

print(reverse_string_easy("Paul is super cool."))
print(reverse_string("Paul is amazing."))
