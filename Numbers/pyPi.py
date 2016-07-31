# Paul Adedeji
# Generate pi up to a certain amount of decimal places (tbd by user).
# A limit of 30 is kept for how far the program will go.

from math import pi

def py_pi():
    # prompt user for nth digit
    n = int(raw_input("What decimal place should this go up to? (highest is 30)? "))

    #cover case of both a input higher than 30 and a negative input
    while n > 30 or n < 0:
        print "Please enter a number less than 30."
        n = int(raw_input("What decimal place should this go up to? (highest is 30)?"))
    #format pi
    else:
        return '%.*f' % (n, pi)

print py_pi()
