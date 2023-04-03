def name_and_price(line):
    parts = line.split(";")
    name = parts[0]
    price = float(parts[2])
    return [name, price]

# Prompt the user for the minimum and maximum prices
min_price = float(input("Enter the minimum price: "))
max_price = float(input("Enter the maximum price: "))

# Read the contents of the file
with open("presents.txt", "r") as file:
    presents = file.readlines()

# Find and print the presents within the specified price range
print("The following presents lie in that price range:")
for present in presents:
    name, price = name_and_price(present.strip())
    if min_price <= price <= max_price:
        print(name)
