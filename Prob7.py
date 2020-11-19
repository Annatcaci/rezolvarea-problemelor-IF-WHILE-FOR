n=int(input("Introduceti varsta lui Mihai "))
b=t=1
c=0
if n<20:
    for i in range(1,n+1):
        b=b*2+i
    print("Mihai la",n,"ani, va primi",b,"$")
elif n>20:
    print("Introducei varsa mai mica ca 20 de ani")
for i in range(1,20):
    while c<=100: 
        c+=c*2+i
        t+=1
print("100$ va primi la",t,"ani")


