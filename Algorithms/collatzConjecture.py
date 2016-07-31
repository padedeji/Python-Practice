# Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def collatz(n, cycles = 0):
    if n<=1:
	    return cycles
    if n % 2 == 0:
        n /= 2
        return str(collatz(n, cycles+1))
    else:
        n = n*3 + 1
        return collatz(n, cycles+1)

inp = int(input("Please give me a number. "))
print("It takes " + str(collatz(inp)) + " steps to reach 1 from " + str(inp) + " using Collatz's conjecture.")
