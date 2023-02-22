def jam():
    # Get the number of large and small jars and the jam amount from the user
    num_large_jars = int(input("Enter the number of large jars: "))
    num_small_jars = int(input("Enter the number of small jars: "))
    jam_amount = int(input("Enter the amount of jam in liters: "))

    # Calculate the total capacity of the large and small jars
    total_capacity = num_large_jars * 5 + num_small_jars * 1

    # Check if the jam amount fits exactly in the jars
    if jam_amount % 5 == 0:
        # If the jam amount is a multiple of 5, use only large jars
        num_used_large_jars = jam_amount // 5
        if num_used_large_jars <= num_large_jars:
            return num_used_large_jars
    elif jam_amount <= total_capacity:
        # If the jam amount is less than the total capacity, use the large jars first
        num_used_large_jars = min(num_large_jars, jam_amount // 5)
        num_used_small_jars = min(num_small_jars, (jam_amount - num_used_large_jars * 5) // 1)
        return num_used_large_jars + num_used_small_jars

    # If the jam amount doesn't fit exactly in the jars, return -1
    return -1

num_used_jars = jam()
print(num_used_jars)