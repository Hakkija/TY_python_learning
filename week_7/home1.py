def calculate_prices(prices, markup):
    marked_up_prices = [p * (1 + markup / 100) for p in prices]
    final_prices = [p * 1.2 for p in marked_up_prices]
    return final_prices
