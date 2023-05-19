from decimal import Decimal, ROUND_HALF_UP


def car_price(price, years):
    if years == 0:
        return round(price, 2)
    else:
        price = Decimal(price) * Decimal('0.8')
        price = price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return float(car_price(price, years - 1))
