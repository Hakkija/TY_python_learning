def read_file(filename):
    results = {}
    with open(filename, "r") as file:
        for line in file:
            round_name, *points = line.strip().split(";")
            results[round_name] = list(map(int, points))
    return results

def find_average(results):
    total_points = 0
    total_rounds = 0
    for points in results.values():
        total_points += sum(points)
        total_rounds += len(points)
    return round(total_points / total_rounds, 1)

def main():
    filename = input("Enter filename: ")
    results = read_file(filename)

    print("The average results of the rounds are:")
    for round_name, points in results.items():
        avg_round = sum(points) / len(points)
        print(f"{round_name}: {avg_round:.1f}")

    overall_average = find_average(results)
    print(f"The average result over all rounds is: {overall_average}")

main()
