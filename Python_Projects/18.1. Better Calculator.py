print("Welcome to Lionel's Basic Calculator")

def calc():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (e.g. +, -, /, *, **,): ")

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        return num1 / num2
    elif operator == "*":
        return num1 * num2
    elif operator == "**":
        return num1 ** num2
    else:
        print("Sorry, the operator is invalid")
        return calc()

print(calc())
