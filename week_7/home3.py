from film import list_films, add_film, delete_film

def process_command(command, args):
    if command == "D":
        genre = args[0]
        films = list_films(genre)
        if films:
            print("Possible films are:")
            for film in films:
                print(film)
        else:
            print(f"No films found for genre {genre}.")
        return True
    elif command == "A":
        genre = args[0]
        name = " ".join(args[1:])
        add_film(name, genre)
        print("Film added!")
        return True
    elif command == "W":
        name = " ".join(args)
        delete_film(name)
        print("Film deleted from the database!")
        print("Happy viewing!")
        return True
    elif command == "E":
        return False


print("=== FILM DATABASE ===")
print("Display films: D <genre>")
print("Add film: A <genre> <film name>")
print("Watch film: W <film name>")
print("Exit: E")
print("===")

while True:
    user_input = input("> ")
    command, *args = user_input.split()
    if not process_command(command, args):
        break
