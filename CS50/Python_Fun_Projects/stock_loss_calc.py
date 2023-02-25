
def get_number_bought_sold():
    while True:
        try:
            number_shares = float(input("Number of shares bought: "))
        except ValueError:
            pass
        else:
            break
    while True:
        try:
            number_bought = float(input("Price bought for: "))
        except ValueError:
            pass
        else:
            break
    while True:
        try:
            number_sold = float(input("Price sold for: "))
        except ValueError:
            pass
        else:
            break

def calc():
    difference_of_sales_amount = float(number_bought - number_sold)
    total_lost = float(difference_of_sales_amount * number_shares)

get_number_bought_sold()