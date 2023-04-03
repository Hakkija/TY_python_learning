import random

def random_position():
    nums = list(range(1, 9))
    random.shuffle(nums)
    return [nums[:4], nums[4:]]

def operation_A(rectangle):
    return [rectangle[0][3:] + rectangle[0][:3], rectangle[1][3:] + rectangle[1][:3]]

def operation_B(rectangle):
    return [rectangle[1], rectangle[0]]

def operation_C(rectangle):
    return [[rectangle[0][0], rectangle[1][0], rectangle[1][2], rectangle[0][3]],
            [rectangle[1][1], rectangle[0][1], rectangle[0][2], rectangle[1][3]]]

def print_rectangle(rectangle):
    for row in rectangle:
        print("    ", " ".join(str(x) for x in row))

rectangle = random_position()

print("The position is")
print_rectangle(rectangle)

while rectangle != [[1, 2, 3, 4], [5, 6, 7, 8]]:
    move = input("Your move: ").strip().upper()

    if move == "A":
        rectangle = operation_A(rectangle)
    elif move == "B":
        rectangle = operation_B(rectangle)
    elif move == "C":
        rectangle = operation_C(rectangle)
    else:
        print("Invalid move, please enter A, B, or C.")

    print("The position is")
    print_rectangle(rectangle)

print("Puzzle is solved!")
