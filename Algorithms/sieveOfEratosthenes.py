# The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
def sieve(array):

    for i in range(len(array)):
      isPrime = True

      for j in range (2, array[i]):

        if array[i] % j == 0:
            isPrime = False
            array[i] = 0
            break

    for i in range(len(array)):

        if array[i] != 0:
            print (array[i])

print (sieve([2,3,4,5,6,7,8]))
