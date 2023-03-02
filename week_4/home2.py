from fractions import Fraction

n = int(input("Enter n: "))

product = 1
for i in range(1, n+1):
    numerator = Fraction(2**(2*i-1), 1)
    denominator = Fraction(2*i, 1) * Fraction(2*i-1, 1)
    fraction = numerator / denominator
    product *= fraction

print("The product is", float(product))
