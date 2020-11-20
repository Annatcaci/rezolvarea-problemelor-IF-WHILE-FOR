from fractions import Fraction
a1=int(input("Introduceti numaratorul primii fractii"))
b1=int(input("Introduceti numitorul primii fractii"))
a2=int(input("Introduceti numaratorul fractiei a doua"))
b2=int(input("Introduceti numitorul fractiei a doua"))
s=Fraction(a1,b1)+Fraction(a2,b2)
p=Fraction(a1,b1)*Fraction(a2,b2)
print(s,p)    

