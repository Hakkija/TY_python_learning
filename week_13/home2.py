class Scooter:
    def __init__(self, name, starting_fee, price_per_100m, distance):
        self.name = name
        self.starting_fee = float(starting_fee)
        self.price_per_100m = float(price_per_100m)
        self.available_distance = int(distance)

    def price(self, length):
        if length <= self.available_distance:
            return self.starting_fee + (length * self.price_per_100m * 10)
        else:
            return 1000

    def ride(self, length):
        if length <= self.available_distance:
            self.available_distance -= length
        else:
            print("Cannot ride that far!")
            self.available_distance = 0

    def charge(self, length):
        self.available_distance += length


class Rental:
    def __init__(self, scooters):
        self.scooters = scooters

    def display_choices(self, length):
        prices = []
        for scooter in self.scooters:
            prices.append((scooter.price(length), scooter.name))
        prices.sort()
        print("Scooters for rent, sorted by price:")
        for i, price in enumerate(prices, start=1):
            print(f"{i}. {price[1]} - {float(price[0]):.1f} euros")

    def rent(self, scooter_name, length):
        for scooter in self.scooters:
            if scooter.name.lower() == scooter_name.lower():
                price = scooter.price(length)
                if price == 1000:
                    print("The battery of the scooter is too low for this ride.")
                else:
                    print(
                        "The price of the ride was {:.1f} euros".format(price))
                    scooter.ride(length)
                return
        print("Invalid scooter name")

    def charge_scooter(self, scooter_name, km):
        for scooter in self.scooters:
            if scooter.name.lower() == scooter_name.lower():
                try:
                    km = int(km)
                except ValueError:
                    print("Invalid value for km: '{}'".format(km))
                    return
                scooter.charge(km)
                return
        print("Invalid scooter name")


# Create three Scooter objects from user input
scooters = []
for i in range(3):
    company, starting_fee, price_per_100m, available_distance = input(
        "Enter company, starting fee, price per hundred meters, and available distance: ").split(", ")
    scooter = Scooter(company, starting_fee,
                      price_per_100m, available_distance)
    scooters.append(scooter)

# Create a Rental object from the Scooter objects
rental = Rental(scooters)

# Display the choices for a ride of length 2 km
rental.display_choices(2)

# Rent a scooter for a ride of length 3 km
rental.rent("Bolt", 3)

# Rent a scooter for a ride of length 18 km
rental.rent("Tuul", 18)

# Rent a scooter for a ride of length 5 km
rental.rent("Tuul", 5)

# Charge a scooter by 5 km
rental.charge_scooter("Tuul", 5)

# Rent a scooter for a ride of length 2 km
rental.rent("Tuul", 2)
