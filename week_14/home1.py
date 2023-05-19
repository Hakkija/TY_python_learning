class Vehicle:
    def __init__(self, brand, price, consumption):
        self.brand = brand
        self.price = price
        self.consumption = consumption

    def __str__(self):
        return f"{self.brand}, price {self.price} euros, fuel consumption {self.consumption} liters per 100 km."

    def trip_cost(self, distance):
        return round(distance / 100 * self.consumption * self.fuel_cost, 1)

    def horsepower(self):
        pass


class Truck(Vehicle):
    _horsepower = 500
    fuel_cost = 1.8

    def horsepower(self):
        return self._horsepower


class Car(Vehicle):
    _horsepower = 180
    fuel_cost = 1.9

    def horsepower(self):
        return self._horsepower


class Motorcycle(Vehicle):
    _horsepower = 85
    fuel_cost = 1.85

    def horsepower(self):
        return self._horsepower


class Garage:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def display(self):
        print("The following vehicles are in the garage:\n")
        for vehicle in self.vehicles:
            print(vehicle)
            print(f"The vehicle has {vehicle.horsepower()} horsepower.")
            print(
                f"It costs {vehicle.trip_cost(186)} euros to travel from Tartu to Tallinn.\n")


def main():
    vehicles = []
    try:
        with open("vehicles.txt", "r") as file:
            for line in file:
                line = line.strip()
                vehicle_type, info = line.split(" - ")
                brand, price, consumption = info.split(", ")
                price = int(price)
                consumption = float(consumption)
                if vehicle_type == "Truck":
                    vehicles.append(Truck(brand, price, consumption))
                elif vehicle_type == "Car":
                    vehicles.append(Car(brand, price, consumption))
                elif vehicle_type == "Motorcycle":
                    vehicles.append(Motorcycle(brand, price, consumption))

        garage = Garage(vehicles)
        garage.display()
    except FileNotFoundError:
        print("The file 'vehicles.txt' was not found.")


if __name__ == "__main__":
    main()
