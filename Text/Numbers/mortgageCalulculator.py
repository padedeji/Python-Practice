# Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan.
import math

def mortgage():
    interest = float(input("What is your monthly interest rate? "))
    i = (interest/100.00)/12.00
    p = float(input("What is the initial amount you borrowed? "))
    n = float(input("What is your payment period (in months)? "))
    m = p*(i*((1 + i)**n)) / (((1 + i)**n)-1)
    x = float(input("How many months have you paid already? "))
    remaining_loan_months = n - x
    return "With a monthly interest rate of %.2f, an intial amount of $%.2f, and a payment period of %.2f months, your monthly mortgage payment is $%.2f, you have paid for %.0f months and you have %.0f months left." % (interest, p, n, m, x, remaining_loan_months)


print (mortgage())
