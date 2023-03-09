username = input("Enter username: ")

while True:
    password = input("Enter password: ")
    if password.isalnum() and len(password) >= 8 and any(char.isdigit() for char in password):
        break
    print("The password must contain both letters and numbers (including at least one digit) and be at least 8 characters long! Try again.")
while True:
    password_again = input("Enter password again: ")
    if password == password_again:
        break
    print("Password do not match! Try again.")

final_password = password[::-1]

print("The password is ", final_password)