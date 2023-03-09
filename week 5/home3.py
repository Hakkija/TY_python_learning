# Read taxi prices from file
with open('taxiprices.txt') as f:
    taxis = [line.strip().split(',') for line in f]

# Ask for distance to home
distance = float(input('Enter distance in kilometers: '))

# Find cheapest taxi
cheapest = None
for name, price_per_km, starting_fee in taxis:
    try:
        price = float(price_per_km) * distance + float(starting_fee)
        if cheapest is None or price < cheapest[1]:
            cheapest = (name, price)
    except ValueError:
        # Skip taxis with invalid prices
        continue

# Print result
if cheapest is None:
    print('No valid taxis found.')
else:
    print(f'{cheapest[0]} is the cheapest.')
    print(f'Taxi fare is computed by the formula kilometer price × distance in kilometers + starting fee.')
