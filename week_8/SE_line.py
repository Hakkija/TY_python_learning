# Read the input heights as a list of integers
heights = list(map(int, input("Enter heights: ").split()))

# Initialize variables to keep track of the maximum number of persons seen and the index of the person who can see the farthest
max_seen = 0
farthest_person = 0

# Iterate through the list of heights
for i in range(len(heights)):
    # Initialize a variable to count the number of persons seen by the current person
    seen = 0
    
    # Iterate through the persons before the current person and count the number of seen persons
    for j in range(i - 1, -1, -1):
        if heights[j] < heights[i]:
            seen += 1
        else:
            break
    
    # Update the maximum number of persons seen and the index of the person who can see the farthest
    if seen > max_seen:
        max_seen = seen
        farthest_person = i

# Print the result
print(f"Person {farthest_person + 1} with height {heights[farthest_person]} can see the farthest.")
