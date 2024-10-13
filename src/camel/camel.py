camel = input("camelCase: ")

for i in camel:
    if i.isupper():
        snake = i.lower()
        print("_", snake, end="", sep="")
        continue
    print(i, end="")

print()
