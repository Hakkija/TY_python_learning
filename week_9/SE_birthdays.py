def find_most_common_birthday(birthdays):
    birthday_counts = {}

    for birthday in birthdays:
        if birthday in birthday_counts:
            birthday_counts[birthday] += 1
        else:
            birthday_counts[birthday] = 1

    max_count = max(birthday_counts.values())

    most_common_birthdays = [date for date, count in birthday_counts.items() if count == max_count]

    return most_common_birthdays


# Sample data
a = ['19.04', '21.05', '04.07', '21.05', '11.11', '12.03', '04.07', '08.06', '12.03', '21.05']

# Find most common birthdays
common_birthdays = find_most_common_birthday(a)

# Print results
print("Most common birthday(s):")
for bday in common_birthdays:
    print(bday)
