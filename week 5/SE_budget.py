def budget(num_people):
    return 10 * num_people + 55

filename = input("Enter file name: ")
invited = []
attending = []
not_attending = []
not_responded = []

with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        if line.endswith("+"):
            invited.append(line[:-1])
            attending.append(line[:-1])
        elif line.endswith("-"):
            invited.append(line[:-1])
            not_attending.append(line[:-1])
        elif line.endswith("?"):
            invited.append(line[:-1])
            not_responded.append(line[:-1])
        else:
            invited.append(line)

total_invited = len(invited)
min_participants = len(attending)
max_participants = len(invited) - len(not_attending)
min_budget = budget(min_participants)
max_budget = budget(max_participants)

print(f"A total of {total_invited} people have been invited")
print(f"The minimum number of participants is {min_participants}")
print(f"The maximum number of participants is {max_participants}")
print(f"The minimum budget for the party is {min_budget} euros")
print(f"The maximum budget for the party is {max_budget} euros")
