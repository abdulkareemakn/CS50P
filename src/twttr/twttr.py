vowels = input("Input: ")

print("Input: ", end="")

for i in vowels:
    if (
        i == "a"
        or i == "e"
        or i == "i"
        or i == "o"
        or i == "u"
        or i == "A"
        or i == "E"
        or i == "I"
        or i == "O"
        or i == "U"
    ):
        continue
    print(i, end="")

print()
