initial_temp = 90  # initial temperature of soup
room_temp = 20  # room temperature
rate = 0.19  # cooling rate per minute

temp = initial_temp
minute = 0

while abs(temp - room_temp) > 1e-7: 
    print(f"After {minute} minute(s), the temperature of the soup is {temp} °C.")
    temp -= rate * (temp - room_temp)
    minute += 1
    if temp <= room_temp:
        break

print(f"The soup has cooled to {temp} °C after {minute} minute(s).")

