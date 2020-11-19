a=eval(input("Introduceti 3 cifre"))
b=eval(input("Introduceti 3 cifre"))
c=eval(input("Introduceti 3 cifre"))
if (a<b+c)and(b<a+c)and(c<b+a):
    if (a!=b)and(b!=c):
        print("Formeaza triunghiul scalen")
    elif (a==b)and(b==c):
        print("Formeaza triunghiul echilateral")
    elif (a==b)or(b!=c):
        print("Formeaza triungiul isoscel")
    elif (c==b)or(b!=a):
        print("Formeaza triungiul isoscel")
    elif (a==c)or(a!=b):
        print("Formeaza triungiul isoscel")
else: 
    print("Nu formeaza un triunghi")