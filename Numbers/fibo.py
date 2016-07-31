# Paul Adedeji
# Generate a user-determined amount of numbers in the Fibonacci sequence

def fibo():
    n = int(raw_input("How many numbers of the Fibonacci sequence should be printed? "))
    fList = []
        #Prevent the use of any number less than 1.
    while n < 1:
        print "Please enter a positive integer greater than 0."
        n = int(raw_input("How many numbers of the Fibonacci sequence should be printed? "))
    for i in range(n):
        # The first two numbers of the Fibonacci sequence are 0 and 1
        if i == 0:
            fList.append(0)
        elif i == 1:
            fList.append(1)
        #Obtain the remaining numbers of the Fibonacci sequence
        else:
            fList.append(fList[i-1] + fList[i-2])
        #print as a string rather than a list
    return str(fList).strip('[]')

print (fibo())
