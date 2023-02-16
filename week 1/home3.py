import math
print("Foot size to number converter.")
name = str.title(input("Enter your name: "))
foot_size = float(input("Enter your foot size (cm): "))

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

converted = round_up(foot_size * 1.5 + 2)
print(f"Dear {name}, your shoe size is {converted}.")