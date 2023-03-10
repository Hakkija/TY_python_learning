with open("prices.txt", "r") as f:
    lines = f.readlines()

total_price = 0
total_items = 0

for line in lines:
    price = float(line.strip())
    total_price += price
    total_items += 1

with open("shopping.txt", "w") as f:
    f.write("The total number of items is {}, with a total price of {:.2f}.".format(total_items, total_price))
    print("Summary written to shopping.txt")

print("The total price of all purchased items is {:.2f}.".format(total_price))
