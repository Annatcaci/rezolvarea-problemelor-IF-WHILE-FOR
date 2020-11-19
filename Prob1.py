n=int(input("Introduceti numarul de zile din luna"))
if n==28:
    print("Februarie intr-un an bisect")
elif n==29:
    print("Februarie intr-un an obisnuit")
elif n==30:
    print("Poate fi luna aprilie, iunie, septembrie, noiembrie")
elif n==31:
    print("Poate fi luna martie, mai, iulie,august,octombrie,decembrie")
else:
    print("Nu exista luna cu",n,"zile")