total = 0

with open("prices.txt", "r") as f:
    for line in f:
        price = float(line.strip())
        total += price

print("The total price of all purchased items is", total)
