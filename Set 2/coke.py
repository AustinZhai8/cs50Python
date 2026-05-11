amountDue = 50

while amountDue > 0:
    print(f"amount due: {amountDue}")
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amountDue -= coin

if amountDue == 0:
    print(f"change owed: {amountDue}")

elif amountDue < 0:
    amountDue *= -1
    print(f"change owed: {amountDue}")