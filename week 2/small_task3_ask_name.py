temperature = float(input("Enter temperature: "))

if temperature < -9:
    print("Frigid")
elif temperature < 0:
    print("Freezing")
elif temperature < 7:
    print("Very cold")
elif temperature < 13:
    print("Cold")
elif temperature < 18:
    print("Cool")
elif temperature < 24:
    print("Comfortable")
elif temperature < 29:
    print("Warm")
elif temperature < 35:
    print("Hot")
else:
    print("Sweltering")
