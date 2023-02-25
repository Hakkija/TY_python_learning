def calculate_pay(hours_worked, hourly_rate):
    if hours_worked <= 40:
        pay = hours_worked * hourly_rate
    else:
        pay = 40 * hourly_rate + (hours_worked - 40) * 1.5 * hourly_rate
    return pay

names =["Arthur the Cat", "Villem E. Veni", "Karmabhumi", "Vicious fish"]
a = list(map(calculate_pay, [50, 40, 45, 35], [6, 8, 7.5, 10]))
print(names[a.index(max(a))])