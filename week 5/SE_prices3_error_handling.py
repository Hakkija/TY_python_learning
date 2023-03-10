total_price = 0
total_items = 0
with open("prices.txt") as f:
    for line in f:
        line = line.strip()
        try:
            price = float(line)
            total_price += price
            total_items += 1
        except ValueError:
            # Skip non-numeric rows
            continue

with open("shopping.txt", "w") as f:
    f.write("The total number of items is {}, with a total price of {:.2f}.".format(total_items, total_price))
print("The total number of items is {}, with a total price of {:.2f}.".format(total_items, total_price))
