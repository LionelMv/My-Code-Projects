num = 1
while num < 20:
    if num % 3 == 0 and num % 5 == 0:
        print("FIzz|Buzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)

    num = num + 1