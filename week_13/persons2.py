class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def bmi(self):
        height = self.height / 100
        return round(self.weight / height**2, 1)


persons = []
with open("healthcheck.txt", "r") as f:
    for line in f:
        name, age, height, weight = line.strip().split(",")
        age = int(age)
        height = int(height)
        weight = int(weight)
        persons.append(Person(name, age, height, weight))

for person in persons:
    bmi = person.bmi()
    category = ""
    if bmi < 19:
        result = "you should gain weight"
    elif bmi > 25:
        result = "you should lose weight"
    else:
        result = "you are of normal weight"
    print(f"{person.name}, {person.age} years old: your body mass index is {bmi}, {result}")
