# Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def collatz(n, cycles = 0):
    if n<=1: # In the event that the input is not greater than 1 the amount of cycles is 0
	    return cycles

    if n % 2 == 0: #If n is even, the amount of cycles will be increased by one, n will be divided by two and the function will rerun using the new n
        n /= 2
        return str(collatz(n, cycles+1))

    else: #If n is odd, the amount of cycles is increased by one, n is multiplied by 3 and increased by one, and the function runs using the new n
        n = (n * 3) + 1
        return collatz(n, cycles+1)

inp = int(input("Please give me a number. "))
print("It takes " + str(collatz(inp)) + " steps to reach 1 from " + str(inp) + " using Collatz's conjecture.")
