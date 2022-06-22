sum = 0
num = float(input("Enter a number: "))
number_of_inputs = 0
def calc(sum, num):



    while num >= 0:
        sum = sum + num
        print(sum)
        return calc(sum, num)

    print("You have input a negative number")