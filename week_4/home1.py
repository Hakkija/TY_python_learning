def number_of_days(month):
    if month < 1 or month > 12:
        return -1
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

while True:
    month_input = input("Enter number of month or 'done': ")
    if month_input == 'done':
        break
    elif not month_input.isdigit():
        print("Please enter a valid number")
        continue
    else:
        month = int(month_input)
        days = number_of_days(month)
        if days == -1:
            print("Number of month must be in the range 1-12")
        else:
            print(f"This month has {days} days")

number_of_days()