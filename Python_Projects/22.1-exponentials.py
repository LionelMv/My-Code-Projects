def raise_to_the_power(base_num, power_num):
    results = 1
    for index in range(power_num):
        results = results * base_num
    return results

print(raise_to_the_power(2,5))