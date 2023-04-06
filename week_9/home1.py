def load_dictionary(filename):
    dictionary = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                word, translation = line.strip().split(" - ")
                dictionary[word] = translation
    except FileNotFoundError:
        with open(filename, "w") as file:
            pass
    return dictionary


def save_dictionary(dictionary, filename):
    with open(filename, "w") as file:
        for word, translation in dictionary.items():
            file.write(f"{word} - {translation}\n")

def main():
    filename = "dictionary.txt"
    open(filename, "w").close()
    dictionary = load_dictionary(filename)

    while True:
        word = input("Enter a word (done to quit): ")
        if word == "done":
            break

        if word in dictionary:
            print(f"{word} means {dictionary[word]}")
        else:
            print(f"There is no information for {word}")
            translation = input(f"What does {word} mean? ")
            dictionary[word] = translation

    print(f"\nThere are {len(dictionary)} entries in the dictionary:")
    for word, translation in dictionary.items():
        print(f"{word} - {translation}")

    save_dictionary(dictionary, filename)

main()
