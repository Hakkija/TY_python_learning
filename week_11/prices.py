
def read_prices(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("; ")
            name = parts[0]
            prices = [float(p) for p in parts[1:]]
            data.append([name] + prices)
    return data

def find_changes(data):
    result = set()
    for item in data:
        name = item[0]
        initial_price = item[1]
        final_price = item[-1]
        price_change = final_price - initial_price
        if price_change != 0:
            result.add((name, initial_price, final_price, price_change))
    return result

def main():
    filename = input("Enter file name: ")
    data = read_prices(filename)
    changes = find_change(data)
    if not changes:
        print("No price change found.")
    else:
        for name, initial_price, final_price, price_change in changes:
            if price_change > 0:
                print(f"The price of {name} increased by {price_change:.2f} euros.")
            else:
                print("The price of {name} decreased by {-price_change:.2f} euros.")
        max_increase = max((c for c in changes), key=lambda x: x[3])
        print("The price of {max_increase[0]} increased the most {max_increase[1]:.2f} ---> {max_increase[2]:.2f} (change {max_increase[3]:.2f} euros).")
main()
