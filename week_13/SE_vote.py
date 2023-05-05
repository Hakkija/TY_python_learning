class Candidate:
    def __init__(self, name: str):
        self.name = name
        self.votes = 0

    def add_vote(self):
        self.votes += 1


class Voter:
    def __init__(self, name: str):
        self.name = name

    def vote(self, candidate: Candidate):
        candidate.add_vote()


# Create the candidates
kaja = Candidate("Kaja")
juri = Candidate("Jüri")
martin = Candidate("Martin")

# Create the voters
jaanus = Voter("Jaanus")
urve = Voter("Urve")
ain = Voter("Ain")
maarja = Voter("Maarja")
siim = Voter("Siim")

# Run the voting process
jaanus.vote(kaja)
urve.vote(juri)
ain.vote(martin)
maarja.vote(kaja)
siim.vote(kaja)
siim.vote(martin)
maarja.vote(juri)
jaanus.vote(juri)
ain.vote(kaja)

# Output the results
print(f"{kaja.name}: {kaja.votes} votes")
print(f"{juri.name}: {juri.votes} votes")
print(f"{martin.name}: {martin.votes} votes")

if kaja.votes > juri.votes and kaja.votes > martin.votes:
    print(f"{kaja.name} wins!")
elif juri.votes > kaja.votes and juri.votes > martin.votes:
    print(f"{juri.name} wins!")
elif martin.votes > kaja.votes and martin.votes > juri.votes:
    print(f"{martin.name} wins!")
else:
    print("There is a tie!")
