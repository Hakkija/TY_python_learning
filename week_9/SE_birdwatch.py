def birds_to_dict(filename):
    bird_dict = {}
    with open(filename, "r") as file:
        for line in file:
            bird, count = line.strip().split(',')
            bird_dict[bird] = int(count)
    return bird_dict

def main():
    filename = input("Enter filename: ")
    bird_dict = birds_to_dict(filename)
    target_frequency = int(input("Enter target frequency: "))
    
    total_birds = 0
    
    for bird, count in bird_dict.items():
        if count > target_frequency:
            print(f"{bird} ({count})")
        total_birds += count
    
    print(f"Juku saw {total_birds} birds outside.")


main()

