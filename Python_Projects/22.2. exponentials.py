
def raise_to_power():
    base_num = int(input("Enter the base number: "))
    power_num = int(input("Enter the power number: "))
    results = 1
    for index in range(power_num):
        results = results * base_num
    return results

print(raise_to_power())