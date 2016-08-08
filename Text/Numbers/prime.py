# Paul Adedeji
# Have the user enter a number and find all Prime Factors (if there are any) and display them.

from math import sqrt

def prime():
	n = int(raw_input("What number do you wish to find the prime factorization of? "))
	fList = []

	while n < 0:
		print "Please enter a positive integer equal to or greater than 0."
		n = int(raw_input("What number do you wish to find the prime factorization of? "))

	else:

		while (n%2==0):
			fList.append(2)
			n /= 2

		for i in range(3, int(sqrt(n)) + 1, 2):
			while (n%i == 0):
				n /= i
				fList.append(i)

		if n > 2:
			fList.append(n)

	return fList

print(prime())
