'''
The program is designed to test Fermat's great theorem
'''

print("Fermat's Great theorem only works with integers, so don't enter floating point numbers.")
a = int(input("Enter the coefficient а: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))
n = int(input("Enter the exponent n (n <= 2): "))

def Ferma(q, w, e, r):
    if n >= 2:
        f = (a**n) + (b**n)
        y = c**n
        if f != y:
            print("The decision is wrong. These values do not solve Fermat's Great Theorem")
        else:
            print("Congratulations. You have found values that satisfy Fermat's Great Theorem")
    else:
        print("The exponent must be equal to 2 or greater")
    pass


Ferma(a, b, c, n)
