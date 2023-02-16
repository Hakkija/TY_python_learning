month = int(input("Enter month number: "))

if month == 12:
    print("winter")
else:
    if month == 1 or month == 2:
        print("winter")
    else:
        if month >= 3 and month <= 5:
            print("spring")
        elif month >= 6 and month <= 8:
            print("summer.")
        else:
            print("autumn.")