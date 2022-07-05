friends = ["Nyaks", "Steve", "Eva", "Denno", "Hadad", "Eva"]
print (friends)
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[2:])
print(friends[1:3])

friends[2] = "Muthoni"
print(friends[2])
#modifying a value in a list

friends2 = friends.copy()

lucky_numbers = [4, 8, 16, 32, 48]
friends.extend(lucky_numbers)
print(friends)
#adding a list to another list.

lucky_numbers.reverse()
print(lucky_numbers)

friends2.append("Alex")
print(friends2)

friends2.insert(2, "Eva")
print(friends2)

friends2.sort()
print(friends2)

friends.remove(4)
print(friends)

friends.pop()
print(friends)
#removes the last value of the list

print(friends2.index("Muthoni"))
print(friends2.count("Eva"))

friends.clear()
print(friends)