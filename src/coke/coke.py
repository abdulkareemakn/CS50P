amount = 50
coin = 0

while True:
    print("Amount Due:", amount)
    coin = int(input("Insert Coin: "))
    if coin == 0 or coin == 5 or coin == 10 or coin == 25:
        amount = amount - coin
        if amount == 0:
            print("Change owed: 0")
            break
        elif amount < 0:
            amount = abs(amount)
            print("Change owed:", amount)
            break
