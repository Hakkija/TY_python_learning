from random import randint

def play(choice1, choice2):
    if choice1 == choice2:
        return "draw"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "paper" and choice2 == "rock") or \
         (choice1 == "scissors" and choice2 == "paper"):
        return "first"
    else:
        return "second"

turns = int(input("Enter number of turns: "))
user_score = 0
computer_score = 0

for i in range(turns):
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = ["rock", "paper", "scissors"][randint(1, 3)-1]
    result = play(user_choice, computer_choice)
    if result == "first":
        user_score += 1
        print(f"Computer chose {computer_choice}. You win! You {user_score}, computer {computer_score}.")
    elif result == "second":
        computer_score += 1
        print(f"Computer chose {computer_choice}. Computer wins! You {user_score}, computer {computer_score}.")
    else:
        print(f"Computer chose {computer_choice}. Draw! You {user_score}, computer {computer_score}.")

if user_score > computer_score:
    print("You won!")
elif user_score < computer_score:
    print("Computer won!")
else:
    print("The game ended in a draw.")
