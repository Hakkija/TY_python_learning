class Record:
    def __init__(self, name, genre, year):
        self.name = name
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.genre}, {self.year}"


class Rock(Record):
    def __init__(self, name, year):
        super().__init__(name, "Rock", year)

    def cost(self, days):
        return 2.5 * days


class Pop(Record):
    def __init__(self, name, year):
        super().__init__(name, "Pop", year)

    def cost(self, days):
        return 1.7 * days


class Classical(Record):
    def __init__(self, name, year):
        super().__init__(name, "Classical", year)

    def cost(self, days):
        return 4.9 * days


class RentalShop:
    def __init__(self, records):
        self.records = records

    def borrow(self):
        money = int(input("How many euros do you have for renting records? "))
        print("------------------------")
        print("Rock music rental costs 2.5 euros per day.")
        print("Pop music rental costs 1.7 euros per day.")
        print("Classical music rental costs 4.9 euros per day.")
        print("------------------------")
        print("Command descriptions:")
        print("L - list the records in the rental")
        print("B <name> <number_of_days> - borrow record")
        print("R <name> <genre> <year> - return record")
        print("E - exit the rental")
        print("------------------------")

        while True:
            print(f"Your balance is {money} euros.")
            command = input("Enter command: ").split()
            if command[0] == 'E':
                break
            elif command[0] == 'L':
                for record in self.records:
                    print(record)
            elif command[0] == 'B':
                record_name = " ".join(command[1:-1])
                days = int(command[-1])
                for i, record in enumerate(self.records):
                    if record.name == record_name:
                        rent = record.cost(days)
                        if money >= rent:
                            money -= rent
                            print(f"{record_name} borrowed.")
                            del self.records[i]
                        else:
                            print("Not enough money for rental!")
                        break
                else:
                    print("No such record in the rental!")
            elif command[0] == 'R':
                record_name = " ".join(command[1:-2])
                genre = command[-2]
                year = int(command[-1])
                if genre == "Rock":
                    self.records.append(Rock(record_name, year))
                elif genre == "Pop":
                    self.records.append(Pop(record_name, year))
                elif genre == "Classical":
                    self.records.append(Classical(record_name, year))
                print(f"{record_name} returned.")
            else:
                print("Invalid command!")


records = [Rock("Nevermind", 1991), Pop("Thriller", 1982),
           Classical("Symphony No. 40", 1788)]
shop = RentalShop(records)
shop.borrow()
