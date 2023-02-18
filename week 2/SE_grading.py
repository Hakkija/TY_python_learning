user_score = input("Enter the final score: ")
grading = input("Enter the grading type (D)ifferentiated or (N)on-differentiated: ")

try:
    user_score = float(user_score)
    if grading.lower() == "d":
        if user_score >= 90:
            grade = "A"
        elif user_score >= 80:
            grade = "B"
        elif user_score >= 70:
            grade = "C"
        elif user_score >= 60:
            grade = "D"
        elif user_score >= 50:
            grade = "E"
        else:
            grade = "F"
        print(f"Your grade is {grade}")
    elif grading.lower() == "n":
        if user_score >= 50:
            print("Congratulations, you have passed the course!")
        else:
            print("Sorry, you have failed the course.")
    else:
        print("Invalid grading type. Please enter '(d)ifferentiated' or '(n)on-differentiated'.")
except ValueError:
    print("Invalid user_score. Please enter a number between 0 and 100.")
