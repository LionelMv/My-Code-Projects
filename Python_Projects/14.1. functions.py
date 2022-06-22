friends = ["Nyaks", "Steve", "Eva", "Denno", "Hadad", "Eva"]
def friends_1():
    #friends = ["Nyaks", "Steve", "Eva", "Denno", "Hadad", "Eva"]
    print(friends)
    print(friends[0])
    print(friends[2])
    print(friends[-1])
    print(friends[2:])
    print(friends[1:3])
    friends[2] = "Muthoni"
    print(friends[2])

friends_1()
print("\n")

def friends_2():
    friends2 = friends.copy()
    friends2.append("Alex")
    print(friends2)
    friends2.insert(2, "Eva")
    print(friends2)
    friends2.sort()
    print(friends2)
    print(friends2.index("Muthoni"))
    print(friends2.count("Eva"))

friends_2()
print("\n")

def num():
    lucky_numbers = [4, 8, 16, 32, 48]
    friends.extend(lucky_numbers)
    print(friends)
    lucky_numbers.reverse()
    print(lucky_numbers)
    friends.remove(4)
    print(friends)
    friends.pop()
    print(friends)
    friends.clear()
    print(friends)

num()
