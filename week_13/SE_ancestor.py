class Person:
    def __init__(self, name: str, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father

    def common_mother(self, other):
        if self.mother is None or other.mother is None:
            return False
        elif self.mother == other.mother:
            return True
        else:
            return self.mother.common_mother(other)

    def common_father(self, other):
        if self.father is None or other.father is None:
            return False
        elif self.father == other.father:
            return True
        else:
            return self.father.common_father(other)

    def ancestor(self, other):
        if self == other:
            return True
        elif self.mother is not None and self.mother.ancestor(other):
            return True
        elif self.father is not None and self.father.ancestor(other):
            return True
        else:
            return False

    def relatives(self, other):
        if self.common_mother(other) or self.common_father(other):
            return True
        elif self.mother is not None and self.mother.relatives(other):
            return True
        elif self.father is not None and self.father.relatives(other):
            return True
        else:
            return False


# Define the Simpson family tree
abe = Person("Abraham")
mona = Person("Mona")
herb = Person("Herb")
clancy = Person("Clancy", father=abe)
jacqueline = Person("Jacqueline")
marge = Person("Marge", mother=jacqueline, father=clancy)
patty = Person("Patty", mother=jacqueline, father=clancy)
selma = Person("Selma", mother=jacqueline, father=clancy)
homer = Person("Homer", mother=mona, father=abe)
herb = Person("Herb", mother=mona, father=abe)
lisa = Person("Lisa", mother=marge, father=homer)
maggie = Person("Maggie", mother=marge, father=homer)
bart = Person("Bart", mother=marge, father=homer)

# Test the methods
print(homer.common_mother(jacqueline))  # True
print(homer.common_father(herb))  # False
print(lisa.ancestor(abe))  # True
print(herb.relatives(maggie))  # False
