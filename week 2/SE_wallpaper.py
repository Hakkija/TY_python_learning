"""In the homework, Mikk had to calculate the number of cans of paint needed to paint the bathroom walls. Next, he decides to put wallpaper on the walls of the living room.

A suitable methodology for finding the number of rolls of wallpaper, which also takes into account the pattern's fit, is the following. For simplicity, we ignore door and window openings.

Based on the perimeter of the living room and the width of the wallpaper, calculate the number of strips needed to cover the walls of the room.
Based on the length of the wallpaper in the roll and the height of the living room, calculate the number of strips from one roll.
Based on the total number of strips and the number of strips in one roll, calculate the number of wallpaper rolls needed.
Write a program that asks the user for the length, width, and height of the living room and the length and width of one roll of wallpaper. The program then finds how many rolls of wallpaper you need to buy to cover the walls of the living room."""


import math

while True:
    try:
        length = float(input("Enter the length of the living room (in meters): "))
        width = float(input("Enter the width of the living room (in meters): "))
        height = float(input("Enter the height of the living room (in meters): "))
        wallpaper_length = float(input("Enter the length of one roll of wallpaper (in meters): "))
        wallpaper_width = float(input("Enter the width of one roll of wallpaper (in meters): "))
        break
    except ValueError:
        print("Invalid input, please enter a numeric value.")


perimeter = 2 * (length + width)
strips = math.ceil(perimeter / wallpaper_width)
strips_per_roll = math.floor(wallpaper_length / height)
rolls = math.ceil(strips / strips_per_roll)
print("You need to buy", rolls, "rolls of wallpaper to cover the walls of the living room.")


