import random


def to_the_sea(blocks):
    if blocks == 0:
        print("Reached the sea")
        return 0

    direction = random.choice(["East", "To the west", "Towards the sea"])
    print(direction)

    if direction == "East" or direction == "To the west":
        return 1 + to_the_sea(blocks)
    else:  # direction == "Towards the sea"
        return 1 + to_the_sea(blocks - 1)


print("Number of blocks walked:", to_the_sea(3))
