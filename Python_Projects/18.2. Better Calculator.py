def calc():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (e.g. +, -, /, *, **,): ")

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "**":
        print(num1 ** num2)
    else:
        print("Sorry, the operator is invalid")
        return calc()