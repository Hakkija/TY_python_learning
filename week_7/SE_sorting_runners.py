def read_registration_data(filename):
    with open(filename) as f:
        data = {int(line.split(".")[0]): line.split(".")[1].strip() for line in f}
    return data

def read_results(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f]

def write_ordered_names(data, results, output_filename):
    with open(output_filename, "w") as f:
        for i, reg_number in enumerate(results, 1):
            f.write(f"{i}. {data[reg_number]}\n")

def main():
    # Get filenames from the user
    registration_filename = input("Enter the registration data filename: ")
    results_filename = input("Enter the results filename: ")

    # Read registration data and results from the files
    registration_data = read_registration_data(registration_filename)
    results = read_results(results_filename)

    # Check if the registration data and results have the same number of entries
    if len(registration_data) != len(results):
        print("Error: The number of entries in the registration data and results files do not match.")
        return

    # Generate the ordered names file
    output_filename = "ordered_names.txt"
    write_ordered_names(registration_data, results, output_filename)

    print(f"Ordered names have been written to {output_filename}")

main()
