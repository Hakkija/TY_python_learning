print("Hello, this is a program that converts numeric values to estonian language")

#data
ones = ["", "üks", "kaks", "kolm", "neli", "viis", "kuus", "seitse", "kaheksa", "üheksa"]
tens = ["", "kümme", "kakskümmend", "kolmkümmend", "nelikümmend", "viiskümmend", "kuuskümmend", "seitsekümmend", "kaheksakümmend", "üheksakümmend"]
teens = ["kümme", "üksteist", "kaksteist", "kolmteist", "neliteist", "viisteist", "kuusteist", "seitseteist", "kaheksateist", "üheksateist"]
#user + some safety if user wants to enter non numeric value.
try:
    num = int(input("Enter a number between 0 and 999: "))
except ValueError:
    print("Invalid input! Please enter a valid number between 0 and 999.")

else:
    if num == 0:
        print("null")
    elif num < 10:
        print(ones[num])
    elif num < 20:
        print(teens[num-10])
    elif num < 100:
        print(tens[num//10] + "-" + ones[num%10])
    else:
        print(ones[num//100] + " sada", end=" ")
        if num % 100 == 0:
            print()
        elif num % 100 < 10:
            print("and " + ones[num%10])
        elif num % 100 < 20:
            print("and " + teens[num%10-10])
        else:
            print("and " + tens[(num//10)%10] + "-" + ones[num%10])
