def budget(num_people):
    food_cost = num_people * 10
    room_rent = 55
    return food_cost + room_rent

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

guest_list = {'+': 0, '-': 0, '?': 0}
total_invited = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if line:
            symbol = line[-1]
            if symbol in guest_list:
                guest_list[symbol] += 1
            total_invited += 1

min_participants = guest_list['+']
max_participants = total_invited - guest_list['-']

min_budget = budget(min_participants)
max_budget = budget(max_participants)

with open(output_file, 'w') as f:
    f.write(f"A total of {total_invited} people have been invited\n")
    f.write(f"The minimum number of participants is {min_participants}\n")
    f.write(f"The maximum number of participants is {max_participants}\n")
    f.write(f"The minimum budget for the party is {min_budget} euros\n")
    f.write(f"The maximum budget for the party is {max_budget} euros\n")

print("Data written to file.")

