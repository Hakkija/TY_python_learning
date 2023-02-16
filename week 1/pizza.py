import math
pizza_size = float(input("What is the dimater of your pizza? "))
pizza_cost = float(input("How many euros does it cost? "))

area = math.pi * pizza_size ** 2 / 4
cm2price = pizza_cost / area * 100

print(f"One square cm of your pizza costs {cm2price} cents.")
