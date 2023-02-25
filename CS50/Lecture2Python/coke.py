amount_due = 50

while amount_due > 0:
    print("Amount Due: ", amount_due)
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin == 5:
        amount_due = amount_due - 5
    elif inserted_coin == 25:
        amount_due = amount_due - 25
    elif inserted_coin == 50:
        amount_due = amount_due - 50
    elif inserted_coin == 10:
        amount_due = amount_due - 10
    else:
        print("Coin not accpeted, try again")
if amount_due == 0:
    print("Change Owed: ", amount_due)
