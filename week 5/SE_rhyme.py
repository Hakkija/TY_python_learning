def score (s, t):
    count = 0
    for i in range(min(len(s), len(t))):
        if s[-i-1] == t[-i-1]:
            count += 1
        else:
            break
    return count

base_word = input("Enter word: ")
score_max = -1
while True:
    word = input("Enter rhyme-word: ")
    if word == "done":
        break
    rhyme_score = score(base_word, word)
    print("Rhyme score is ", rhyme_score)
    if rhyme_score > score_max:
        score_max = rhyme_score
        word_max = word
print(f"The word with the highest rhyme score was {word_max}, "
      f"with score {score_max}")