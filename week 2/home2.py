def get_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    if month_number <= 0:
        return "Month number must be in the range [1-12]"
    if month_number >= 13:
        return "The year has only 12 months"
    return months[month_number-1]

def main():
    month_number_client = input("Enter the month number (1-12): ")
    try:
        month_number = int(month_number_client)
    except:
        month_number = -1
        print("Please enter a number!")
    month_name = get_month_name(month_number)
    print(month_name)
    
main()


