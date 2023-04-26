import requests
import json
import matplotlib.pyplot as plt
from collections import defaultdict

url = "https://opendata.digilugu.ee/opendata_covid19_test_county_all.json"
response = requests.get(url)
data = json.loads(response.text)

# Choose the county you want to analyze
county_name = "Harju maakond"

# Collect data for the county
county_data = defaultdict(lambda: {"positive": 0, "total": 0})
for entry in data:
    if entry["County"] == county_name:
        if entry["ResultValue"] == "P":
            county_data[entry["StatisticsDate"]]["positive"] += entry["Total"]
        county_data[entry["StatisticsDate"]]["total"] += entry["Total"]

# Prepare data for plotting
dates = sorted(county_data.keys())
positive_tests = [county_data[date]["positive"] for date in dates]
total_tests = [county_data[date]["total"] for date in dates]
positive_percentage = [100 * p / t for p, t in zip(positive_tests, total_tests)]

# Plot total number of positive tests
plt.figure(figsize=(12, 6))
plt.plot(dates, positive_tests, marker="o")
plt.title(f"Total number of positive tests in {county_name}")
plt.xlabel("Date")
plt.ylabel("Number of positive tests")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Plot percentage of positive tests
plt.figure(figsize=(12, 6))
plt.plot(dates, positive_percentage, marker="o")
plt.title(f"Percentage of positive tests in {county_name}")
plt.xlabel("Date")
plt.ylabel("Percentage of positive tests")
plt.xticks(rotation=45)
plt.grid()
plt.show()
