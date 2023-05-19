import random


class Dragon:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name} roars")


class EarthDragon(Dragon):
    def __init__(self, name, energy):
        super().__init__(name)
        self.energy = energy

    def attack(self):
        if self.energy > 0:
            print(f"{self.name} shakes the ground")
            self.energy -= 1
        else:
            super().attack()


class FireDragon(Dragon):
    def __init__(self, name, fuel):
        super().__init__(name)
        self.fuel = fuel

    def attack(self):
        if self.fuel >= 10:
            print(f"{self.name} spits fire")
            self.fuel -= 10
        else:
            super().attack()


class StoneDragon(EarthDragon):
    def __init__(self, name, energy, stones):
        super().__init__(name, energy)
        self.stones = stones

    def attack(self):
        if self.stones > 0:
            stones_to_throw = min(self.stones, 3)
            print(f"{self.name} throws {stones_to_throw} stones")
            self.stones -= stones_to_throw
        else:
            super().attack()


class LavaDragon(FireDragon):
    def __init__(self, name, fuel, lava):
        super().__init__(name, fuel)
        self.lava = lava

    def attack(self):
        if self.lava > 0:
            lava_to_spew = min(self.lava, random.randint(1, 100))
            print(f"{self.name} spews {lava_to_spew} units of lava")
            self.lava -= lava_to_spew
        else:
            super().attack()


# Main program
dragons = [StoneDragon("StoneDragon1", 4, 6), StoneDragon("StoneDragon2", 3, 5), LavaDragon(
    "LavaDragon1", 30, 200), LavaDragon("LavaDragon2", 25, 150)]

for _ in range(10):
    dragon = random.choice(dragons)
    dragon.attack()
