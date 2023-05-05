def get_digit_segments(digit, size):
    segments = []
    if digit == 0:
        segments = [" " + "-" * size + " ", "|" + " " * (size + 1) + "|", "|" + " " * (size + 1) + "|", " " * (
            size + 2), "|" + " " * (size + 1) + "|", "|" + " " * (size + 1) + "|", " " + "-" * size + " "]
    elif digit == 1:
        segments = [" " * (size + 2), " " * (size + 1) + "|", " " * (size + 1) + "|", " " * (
            size + 2), " " * (size + 2), " " * (size + 1) + "|", " " * (size + 1) + "|"]
    elif digit == 2:
        segments = [" " + "-" * size + " ", " " * (size + 1) + "|", " " * (size + 1) + "|", " " + "-" * size + " ", "|" + " " * (
            size + 1) + " ", "|" + " " * (size + 1) + " ", " " + "-" * size + " "]
    elif digit == 3:
        segments = [" " + "-" * size + " ", " " * (size + 1) + "|", " " * (
            size + 1) + "|", " " + "-" * size + " ", " " * (size + 1) + "|", " " * (size + 1) + "|", " " + "-" * size + " "]
    elif digit == 4:
        segments = [" " * (size + 2), "|" + " " * (size + 1) + "|", "|" + " " * (size + 1) + "|",
                    " " + "-" * size + " ", " " * (size + 2), " " * (size + 1) + "|", " " * (size + 1) + "|"]
    elif digit == 5:
        segments = [" " + "-" * size + " ", "|" + " " * (size + 1) + " ", "|" + " " * (
            size + 1) + " ", " " + "-" * size + " ", " " * (size + 1) + "|", " " * (size + 1) + "|", " " + "-" * size + " "]
    elif digit == 6:
        segments = [" " + "-" * size + " ", "|" + " " * (size + 1) + " ", "|" + " " * (
            size + 1) + " ", " " + "-" * size + " ", "|" + " " * (size + 1) + "|", "|" + " " * (size + 1) + "|", " " + "-" * size + " "]
    elif digit == 7:
        segments = [" " + "-" * size + " ", " " * (size + 1) + "|", " " * (size + 1) + "|", " " * (
            size + 2), "|" + " " * (size + 2), "|" + " " * (size + 2), "|" + " " * (size + 2)]
    elif digit == 8:
        segments = [" " + "-" * size + " ", "|" + " " * (size + 1) + "|", "|" + " " * (
            size + 1) + "|", " " + "-" * size + " ", "|" + " " * (size + 1) + "|", "|" + " " * (size + 1) + "|", " " + "-" * size + " "]
    elif digit == 9:
        segments = [" " + "-" * size + " ", "|" + " " * (size + 1) + "|", "|" + " " * (
            size + 1) + "|", " " + "-" * size + " ", " " * (size + 1) + "|", " " * (size + 1) + "|", " " + "-" * size + " "]
    return segments


def display_digit(number, size):
    segments = get_digit_segments(number, size)
    for i in range(len(segments)):
        if i == 0:
            print(" " + segments[i], end="")
        elif i == 3:
            print(" " * size + segments[i], end="")
        else:
            print(segments[i] + " " * size, end="")
        if i == 2 or i == 4:
            print(" ", end="")
        else:
            print(" " * size, end="")
    print()


def display_number(number, size):
    digits = [int(d) for d in str(number)]
    digit_segments = [get_digit_segments(d, size) for d in digits]
    display_segments = [[] for _ in range(2*size+3)]

    for d in digit_segments:
        for i, s in enumerate(d):
            display_segments[i].append(s)

    for s in display_segments:
        print("".join(s))


number = int(input("Enter number: "))
size = int(input("Enter size: "))
display_number(number, size)
