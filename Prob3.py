n=int(input("Introduceti n"))
m=int(input("Introduceti m"))
from decimal import Decimal 
if m>n:
    print("A-ti introdus gresit. M trebuie sa fie mai mic ca n.")
if n>m:
    for i in range(1,1000):
        if m**i==n:
            print("n este puterea lui m")
