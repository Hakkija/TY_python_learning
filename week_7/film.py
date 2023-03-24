def list_films(genre):
    with open("films.txt") as f:
        lines = f.readlines()
        films = []
        for line in lines:
            name, g = line.strip().split(" - ")
            if g == genre:
                films.append(name)
        return films

def add_film(name, genre):
    with open("films.txt", "a") as f:
        f.write(name + " - " + genre + "\n")

def delete_film(name):
    with open("films.txt", "r") as f:
        lines = f.readlines()
    with open("films.txt", "w") as f:
        for line in lines:
            if not line.startswith(name):
                f.write(line)
