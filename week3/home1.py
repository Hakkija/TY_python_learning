import math

def cake_price(cake_name=None, cake_size=None):
    if cake_name is None:
        # Prompt the user for the cake name and size if not provided
        cake_name = input("Enter the cake name: ")
        cake_size = input("Enter the cake size (in cm): ")

    if cake_name.lower() == 'chocolate cake':
        # Calculate the price of a chocolate cake based on the radius
        radius = float(cake_size)
        area = math.pi * radius**2
        price = round(area * 0.05, 2)
        return (0, price)
    elif cake_name.lower() == 'strawberry cake':
        # Calculate the price of a strawberry cake based on the radius
        radius = float(cake_size)
        area = math.pi * radius**2
        price = round(area * 0.04, 2)
        return (0, price)
    elif cake_name.lower() == 'napoleon cake':
        # Calculate the price of a Napoleon cake based on the side length
        length = float(cake_size)
        area = length**2
        price = round(area * 0.08, 2)
        return (0, price)
    else:
        # Return an error code if the cake name is invalid
        return (-1, None)

def print_result(result):
    code, price = result
    if code == 0:
        print("The price of the cake is", price, "euros.")
    else:
        print("Invalid cake name.")

# Prompt the user for the cake name and size, calculate the price, and print the result
result = cake_price()
print_result(result)
