while True:
    fraction = input("Fraction: ")

    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        x / y
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if x > y:
            continue
        break

fuel = x / y * 100

if fuel >= 99:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(f"{fuel:.0f}%")
