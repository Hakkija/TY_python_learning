import requests

def read_exchange_rates(url):
    exchange_rates = {}
    response = requests.get(url)
    content = response.text.splitlines()
    
    for line in content:
        data = line.strip().split('\t')
        currency_code, _, rate = data
        exchange_rates[currency_code] = float(rate)
    
    return exchange_rates

url = "https://courses.cs.ut.ee/2023/progeng/spring/uploads/Main/rates.txt"
exchange_rates = read_exchange_rates(url)
all_rates = calculate_exchange_rates(exchange_rates)


def convert_currency(amount, source, target, rates_dict):
    source_to_eur = 1 / rates_dict[source] if source != 'EUR' else 1
    target_to_eur = rates_dict[target] if target != 'EUR' else 1
    return amount * source_to_eur / target_to_eur

filename = "rates.txt"
exchange_rates = read_exchange_rates(filename)
all_rates = calculate_exchange_rates(exchange_rates)

while True:
    source_currency = input("Enter source currency: ")
    if source_currency.lower() == "done":
        break

    target_currency = input("Enter target currency: ")
    if target_currency.lower() == "done":
        break

    amount = float(input("Enter the amount to be converted: "))
    converted_amount = convert_currency(amount, source_currency, target_currency, all_rates[source_currency])
    print(f"{amount} {source_currency} is equivalent to {converted_amount:.4f} {target_currency}")
