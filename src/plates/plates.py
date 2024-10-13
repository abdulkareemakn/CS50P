def main():
    plate = input("Plate: ")
    if (
        is_valid(plate)
        and validLength(plate)
        and checkGrammar(plate)
        and checkNum(plate)
        and checkZero(plate)
    ):
        print("Valid")
    else:
        print("Invalid")


def validLength(s):
    if 2 <= len(s) <= 6:
        return True


def checkGrammar(s):
    if s.isalnum():
        return True
    else:
        return False


def checkNum(s):
    if s.isalnum():
        if s[-1].isalpha():
            return False
    return True


def checkZero(s):
    for i in s:
        if i.isdigit():
            if i == 0:
                return False
            return True


def is_valid(s):
    first_two = s[0:2]
    if first_two.isalpha():
        return True


main()
