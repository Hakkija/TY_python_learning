def find_infection_origins(data):
    infected_by = {i + 1: data[i] for i in range(len(data))}
    origins = set()

    for person, infector in infected_by.items():
        if infector == 0:
            continue
        if infector not in infected_by or infected_by[infector] == 0:
            origins.add(infector)

    return origins

data = [16, 51, 27, 42, 22, 0, 0, 0,
        3, 44, 0, 39, 42, 10, 25,
        38, 0, 33, 29, 0, 0, 3, 0,
        19, 24, 0, 39, 0, 33, 13, 6,
        0, 6, 0, 0, 0, 38, 31, 31,
        0, 10, 10, 0, 6, 51, 0, 0,
        0, 0, 0, 33, 0, 33, 10, 0]

origins = find_infection_origins(data)

print("Starting point(s) of the spread of infection:", " ".join(map(str, sorted(origins))))
