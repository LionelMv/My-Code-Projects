print("Giraffe\nAcademy")
print("Giraffe \"Academy\"")

phrase = "Giraffe Academy"
print("\n" + phrase)
print("\t" + phrase)
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
#changes the string into uppercase then checks the new string if it is uppercase.

print(len(phrase))
#prints the length of the string.

print(phrase[0])
#prints the first letter on the string. Python starts at index 0

print(phrase.index("G"))
print(phrase.index("Acad"))
#prints the location/index of where the string starts.

print(phrase.replace("Giraffe", "Elephant"))
