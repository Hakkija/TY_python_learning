import random
import matplotlib.pyplot as plt

def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

# Generate a random point
target = (random.randint(0, 100), random.randint(0, 100))
attempts = 0
path_x = []
path_y = []

while True:
    # Get the user's guess
    user_x = int(input("Enter your guess for x: "))
    user_y = int(input("Enter your guess for y: "))
    guess = (user_x, user_y)
    attempts += 1
    path_x.append(user_x)
    path_y.append(user_y)

    # Check if the guess is correct
    if guess == target:
        print(f"Congratulations! You guessed the point in {attempts} attempts.")
        break
    else:
        # Calculate the distance and provide feedback
        dist = distance(guess, target)
        print(f"Your guess is {dist:.2f} units away from the target. Try again.")

# Plot the guessing path
plt.plot(path_x, path_y, marker='o', linestyle='-')
plt.scatter(*target, color='red', marker='x', label='Target')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Guessing Path')
plt.show()
