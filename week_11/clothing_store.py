
def read_inventory(filename):
    inventory = {}
 #   print(inventory)
    with open(filename, "r") as f:
        for line in f:
 #           print(line)
            data = line.strip().split("; ")
            if data[-1] == "good":
                code, name, color, price = data[:4]
                inventory[code] = [name, color, float(price)]
    return inventory
def products(inventory):
    product_dict = {}
    for code, data in inventory.items():
        name, color, price = data
        if name not in product_dict:
            product_dict[name] = []
        product_dict[name]. append((color, price, code))
    return product_dict
    
def main():
    filename = "inventory.txt"
    inventory = read_inventory(filename)
    name = input("Enter product name: ")
    max_price = float(input("Enter maximum price: "))
    suitable_products = []
    for color, price, code in products(inventory).get(name, []):
        if price <= max_price:
            suitable_products.append((code, name, color, price))
    if len(suitable_products) == 0:
        print("No suitable product found.")
    else:
        for product in suitable_products:
            print(*product)

main()
        