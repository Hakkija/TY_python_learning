def max_bottles(money, price, deposit):
    total_price = price + deposit
    bottles = int(money // total_price)

    if bottles == 0:
        return 0

    remaining_money = money - (bottles * total_price)
    return_bottle_money = bottles * deposit

    return bottles + max_bottles(remaining_money + return_bottle_money, price, deposit)
