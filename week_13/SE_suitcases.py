class Item:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def output_item(self):
        print(f"{self.name}, {self.weight} kg")


class Suitcase:
    def __init__(self, weight_limit: float):
        self.weight_limit = weight_limit
        self.items = []
        self.total_weight = 0

    def add_item(self, item: Item):
        if self.total_weight + item.weight > self.weight_limit:
            print("Weight limit exceeded!")
        else:
            self.items.append(item)
            self.total_weight += item.weight

    def output_summary(self):
        item_count = len(self.items)
        print(
            f"There are {item_count} items in the suitcase with a total weight of {self.total_weight} kg.")

    def output_items(self):
        for item in self.items:
            item.output_item()


class LuggageRoom:
    def __init__(self, weight_limit: float):
        self.weight_limit = weight_limit
        self.suitcases = []
        self.total_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if self.total_weight + suitcase.total_weight > self.weight_limit:
            print("Weight limit exceeded!")
        else:
            self.suitcases.append(suitcase)
            self.total_weight += suitcase.total_weight

    def output_summary(self):
        suitcase_count = len(self.suitcases)
        free_space = self.weight_limit - self.total_weight
        print(
            f"There are {suitcase_count} suitcases in the luggage room with {free_space} kg of free space.")

    def output_items(self):
        for suitcase in self.suitcases:
            suitcase.output_items()


# Create some items
laptop = Item("Laptop", 2)
book = Item("Book", 1)
dumbbell = Item("Dumbbell", 4)

# Create a suitcase and add the items to it
suitcase = Suitcase(5)
suitcase.add_item(laptop)
suitcase.output_summary()
suitcase.add_item(book)
suitcase.output_summary()
suitcase.add_item(dumbbell)
suitcase.output_summary()
suitcase.output_items()

# Create a luggage room and add the suitcase to it
luggage_room = LuggageRoom(50)
luggage_room.add_suitcase(suitcase)
luggage_room.output_summary()
luggage_room.output_items()
