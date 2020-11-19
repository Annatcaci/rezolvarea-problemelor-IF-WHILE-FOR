n=int(input("Introduceti un numar"))
for i in range(1,n):
    e=0
    for m in range(1,i):
        if i%m==0:
            e+=m
    if e==i:
        print("Numarul perfect este",i)

