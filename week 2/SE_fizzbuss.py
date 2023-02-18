"""
1. Fizzbuzz
(1/2) Write a program that asks the user for an integer.

If the number is divisible by 3, then it prints "Fizz".
If it is divisible by 5, then it prints "Buzz".
If it is divisible by both 3 and 5, then it prints "FizzBuzz".
Otherwise, it prints the same number.
"""

num = int(input("Enter an integer: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
