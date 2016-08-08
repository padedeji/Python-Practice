#Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
def stats(fileName):
    inFile=open(fileName)
    contents=inFile.read()
    numWord=1 #Since this program counts spaces we must start with 1 to account for the lack of space in front of the first word.
    for character in contents:
        if character is " ":
            numWord+=1
    return "There are %.i words in the file." % numWord
    inFile.close()
print(stats('practice.txt'))
