dragons = int(input("Enter number of dragons: "))
snakes = int(input("Enter number of snakes: "))
dinosaurs = int(input("Enter number of dinosaurs: "))

day = 0
while sum(x > 0 for x in [dragons, snakes, dinosaurs]) >= 2:
    snakes = max(snakes - dragons, 0)
    dinosaurs = max(dinosaurs - snakes, 0)
    dragons = max(dragons - dinosaurs, 0)
    day += 1
print("The last meal will be on day" , day)

if dragons > 0:
    print("There will be ", dragons, "dragons left.")
if snakes > 0:
    print("There will be ", snakes, "dragons left.")
if dinosaurs > 0:
    print("There will be ", dinosaurs, "dragons left.")
