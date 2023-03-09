# Open the file for reading
with open("prices.txt", "r") as f:
    # Read the contents of the file into a list
    lines = f.readlines()

# Initialize the dictionary to store the products and their prices
products = {}

# Loop through the lines of the file and extract the product names and prices
for i in range(0, len(lines), 2):
    # Remove any leading or trailing whitespace from the product name
    product_name = lines[i].strip()
    # Try to convert the price to a float
    try:
        price = float(lines[i+1].strip())
    except ValueError:
        # If the price can't be converted to a float, set it to None
        price = None
    # Add the product name and price to the dictionary
    products[product_name] = price

# Compute the new prices and print them on the screen
for product_name, price in products.items():
    # Check if the price is None (couldn't be converted to a float)
    if price is None:
        print(f"Cannot convert the price for {product_name}.")
    else:
        # Compute the new price by subtracting 10% from the original price
        new_price = price * 0.9
        # Print the product name and the new price, rounded to 2 decimal places
        print(f"New price for {product_name} is {round(new_price, 2)} euros.")
