for school in "Giraffe Academy":
    print(school)
print("\n")

friends = ["Eva", "Nyaks", "Hadad"]
print(len(friends))
for friend in friends:
    print(friend)
#note that school and friend are variables and can be changed to anything.
print("\n")

for index in range(10):
    print(index)
#does not include 10, starts with 0
print("\n")

for index in range(3,10):
    print(index)

print("\n")
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not the first")