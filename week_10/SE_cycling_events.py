def read_participants(filename):
    with open(filename, 'r') as file:
        participants = set(line.strip() for line in file.readlines())
    return participants

# Get the number of events from the user
num_events = int(input("Enter number of events: "))

all_participants = set()
prev_participants = set()
max_newcomers = 0
max_newcomers_event = 0

for i in range(1, num_events + 1):
    event_file = f"event{i}.txt"
    participants = read_participants(event_file)
    all_participants.update(participants)

    if i > 1:
        newcomers = participants - prev_participants
        if len(newcomers) > max_newcomers:
            max_newcomers = len(newcomers)
            max_newcomers_event = i

    prev_participants = participants

# Print the event with the most number of newcomers
print(f"Event {max_newcomers_event} attracted the most number of newcomers, {max_newcomers} newcomers.")
