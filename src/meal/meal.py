def main():
    time = input("What time is it? ")

    hours = convert(time)

    print(hours)
    # minutes = int(minutes)

    if 7 >= hours <= 8:
        print("breakfast time")

    elif 12 >= hours <= 13:
        print("lunch time")

    elif 18 >= hours <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    minutes = minutes / 60

    return hours + minutes


if __name__ == "__main__":
    main()