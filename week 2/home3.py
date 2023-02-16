def calculate_paint_needed(length, width, height, paint_volume):
    wall_area = (length * height * 2) + (width * height * 2)
    paint_needed = wall_area / 8
    cans_needed = paint_needed / paint_volume
    return cans_needed

def main():
    length = float(input("Enter the length of the bathroom (in meters): "))
    width = float(input("Enter the width of the bathroom (in meters): "))
    height = float(input("Enter the height of the bathroom (in meters): "))
    paint_volume = float(input("Enter the volume of paint in one can (in liters): "))
    cans_needed = calculate_paint_needed(length, width, height, paint_volume)
    print("You will need to buy", cans_needed, "cans of paint.")

main()
