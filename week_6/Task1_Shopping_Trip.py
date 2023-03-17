filename = input("Enter file name: ")

#
#prompts the user for the name of the data file;
#prompts the user for the name of a food item that will not be bought;
not_to_buy = input("What not to buy: ")

#- if there is no such food item in the file, all food items are bought;
#writes the names of the food items to be bought on the screen;
#prints the total cost of the purchase on the screen, rounded to two decimal places;
#prints the information on the screen on whether Priit had enough money;
#determines how much money Priit had short or left over and writes this to file money.txt.
#
with open(filename, "r") as f:
    items = []
    total_cost = 0.0
    
    for line in f:
        name = line.strip()
        price = float(f.readline().strip())
        quantity = int(f.readline().strip())
        
        if name != not_to_buy:
            items.append(name)
            total_cost += price * quantity
#enough money---------15 eur
if total_cost <= 15.0:
    enough_money = True
else:
    enough_money = False
print("Shopping list: " + ", ".join(items))
print("The total cost of the purchase is " + "{:.2f}".format(total_cost) + " EUR.")

if enough_money:
    print("Priit had enough money to go Shopping!!")
    with open("money.txt", "w") as f:
        f.write("Priit had " + "{:.2f}".format(15.0 - total_cost) + " EUR left over.")
else:
    print("Priit didn't have enough money to go shopping!!")
    with open("money.txt", "w") as f:
        f.write("Priit had " + "{:.2f}".format(total_cost - 15.0) + " EUR short.")
