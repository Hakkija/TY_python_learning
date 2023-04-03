# Get user input
item_counts = input("Enter the numbers of items: ")

# Convert input to a list of integers
item_counts_list = [int(x) for x in item_counts.split()]

# Calculate the number of people in the queue
num_people = len(item_counts_list)

# Count the number of people with more than three items
num_people_more_than_three = sum(1 for x in item_counts_list if x > 3)

# Find the person with the most items and their number of items
max_items = max(item_counts_list)
person_with_most_items = item_counts_list.index(max_items) + 1

# Output the results
print(f"There are {num_people} people standing in the queue")
print(f"{num_people_more_than_three} people have more than three items in their baskets")
print(f"Person number {person_with_most_items} has the most items, {max_items} items")
