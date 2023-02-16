def calculate_fine(limit, speed, max_fine):
    fine = 0
    over_limit = speed - limit
    if over_limit <= 0:
        return fine
    else:
        fine = over_limit * 3
    if fine > max_fine:
        return max_fine
    return fine

def main():
    name = input("Enter your name: ")
    limit = int(input("Enter the speed limit: "))
    speed = int(input("Enter your actual speed: "))
    max_fine = 190
    fine = calculate_fine(limit, speed, max_fine)
    if fine > 0:
        print(f"{name}, your fine is {fine}€.")
    else:
        print(f"{name}, you were driving within the speed limit.")

main()
