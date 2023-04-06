def read_words(filename):
    with open(filename, "r") as file:
        words = file.read().splitlines()
    return words

def next_guess(guessed_letters, possible_words):
    letter_frequency = {}
    for word in possible_words:
        for letter in word:
            if letter not in guessed_letters:
                letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

    return max(letter_frequency, key=letter_frequency.get)

def filter_possible_words(guessed_word, possible_words):
    return [
        word for word in possible_words
        if len(word) == len(guessed_word)
        and all(c1 == c2 or c2 == "_" for c1, c2 in zip(word, guessed_word))
    ]

def main():
    all_words = read_words("corncob_caps.txt")
    guessed_word = input()
    guessed_letters = set()

    possible_words = filter_possible_words(guessed_word, all_words)

    while "_" in guessed_word:
        guess = next_guess(guessed_letters, possible_words)
        guessed_letters.add(guess)
        print(guess)

        clue = input()
        if clue == guessed_word:
            break

        for i, c in enumerate(clue):
            if c != "_":
                guessed_word = guessed_word[:i] + c + guessed_word[i + 1:]

        possible_words = filter_possible_words(guessed_word, possible_words)

    print(guessed_word)

main()
