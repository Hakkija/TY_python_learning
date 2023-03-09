for dragons in range(1, 1000):
for snakes in range(1, 1000):
for dinosaurs in range(1, 1000):
    day = 0
        while dragons > 0 and day < 365:
                snakes_eaten = min(snakes, dragons)
                dinosaurs_eaten = min(dinosaurs, snakes)
                dragons_eaten = min(dragons, dinosaurs)
                snakes -= snakes_eaten
                dinosaurs -= dinosaurs_eaten
                dragons -= dragons_eaten
                day += 1
            if day == 365 and sum([dragons, snakes, dinosaurs]) > 0:
                print("Initial number of dragons:", dragons)
                print("Initial number of snakes:", snakes)
                print("Initial number of dinosaurs:", dinosaurs)