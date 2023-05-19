import math


class Cake:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def area(self):
        return self.size ** 2

    def cm2price(self):
        return round((self.price / self.area()) * 100, 2)


class RoundCake(Cake):
    def area(self):
        radius = self.size / 2
        return math.pi * (radius ** 2)


class Pizza(RoundCake):
    def __init__(self, name, size, price, cover_price):
        super().__init__(name, size, price)
        self.cover_price = cover_price

    def cm2price(self):
        total_price = self.price + self.cover_price
        return round((total_price / self.area()) * 100, 2)


def cheapest_cake(cakes):
    min_price = float('inf')
    cheapest_cake = None

    for cake in cakes:
        if cake.cm2price() < min_price:
            min_price = cake.cm2price()
            cheapest_cake = cake.name

    return cheapest_cake


# Create cakes
c1 = Cake("Blueberry cake", 8, 3.52)
c2 = RoundCake("Carrot-pumpkin pizza base", 24, 1.85)
c3 = Pizza("Caesar Pizza", 24, 1.85, 6.70)

cakes = [c1, c2, c3]

# Find the cake with the lowest price per square centimeter
print(cheapest_cake(cakes))
