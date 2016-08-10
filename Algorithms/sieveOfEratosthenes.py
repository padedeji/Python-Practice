# The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
def sieve(array):

    for i in range(len(array)): #Assume that every item in the array is prime
      isPrime = True

      for j in range (2, array[i]): # if factor is prime then multiples are marked as non-prime and turned into 0

        if array[i] % j == 0:
            isPrime = False
            array[i] = 0
            break

    for i in range(len(array)): #any number that is not 0 is prime

        if array[i] != 0:
            print (array[i])

print (sieve([2,3,4,5,6,7,8]))
