import math

def number_of_skeins(skein_weight, scarf_lenght):
    yarn_needed = scarf_lenght * 105  #grams
    return math.ceil(yarn_needed / skein_weight)

def knitting_time(scarf_lenght, working_hours_per_week):
    scarf_lenght_cm = scarf_lenght * 100
    hours_needed = scarf_lenght_cm / 20
    return math.ceil(hours_needed / working_hours_per_week)

scarf_lenght = float(input("Enter the length of the scarf in meters: "))
skein_weight = int(input("Enter the weight of one skein in grams: "))
skein_price = float(input("Enter the price of one skein in euros: "))
working_hours_per_week = int(input("Enter the number of working hours per week: "))

skeins_needed = number_of_skeins(skein_weight, scarf_lenght)
total_price = skeins_needed * skein_price
weeks_needed = knitting_time(scarf_lenght, working_hours_per_week)

print(f"You will need {skeins_needed} skeins of yarn, which costs a total of {total_price:.2f} euros.")
print(f"It takes {weeks_needed} weeks to knit.")
      