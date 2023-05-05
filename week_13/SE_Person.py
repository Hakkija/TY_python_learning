class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def bmi(self) -> float:
        height_in_m = self.height / 100
        bmi = self.weight / (height_in_m ** 2)
        return round(bmi, 1)


with open("healthcheck.txt") as file:
    people = []
    for line in file:
        try:
            name, age, height, weight = line.strip().split(", ")
            person = Person(name, int(age), int(height), int(weight))
            people.append(person)
        except ValueError:
            print(f"Invalid data in line: {line.strip()}")

for person in people:
    bmi = person.bmi()
    status = ""
    if bmi < 19:
        status = "you should gain weight"
    elif bmi > 25:
        status = "you should lose weight"
    else:
        status = "you are of normal weight"
    print(f"{person.name}, {person.age} years old: your body mass index is {bmi}, {status}")
