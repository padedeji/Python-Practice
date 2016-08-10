# A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

def calculate(operator, n1, n2):
    if operator not in "*-+/": #This calculator only does basic operations so anything past multiplication, subtraction, addition, and division is not accepted
        return input("Please enter a basic math operator. ")

    elif operator == "*": 
        return "%.i * %.i = %.i" % (n1, n2, n1*n2)

    elif operator == "-":
        return "%.i - %.i = %.i" % (n1, n2, n1-n2)

    elif operator == "+":
        return "%.i + %.i = %.i" % (n1, n2, n1+n2)

    elif operator == "/":
        return "%.i / %.i = %.i" % (n1, n2, n1/n2)


n1 = int(input("What is the first number? "))
n2 = int(input("What is the second number? "))
operator = raw_input("What math operator would you like to use? (Please choose from *, -, +, and /) ")
print(calculate(operator, n1, n2))
