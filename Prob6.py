n=int(input("Introduceti un numar"))
s1=s2=s3=s4=a=b=0
for i in range(1,n+1):
    s1+=i**3  
    s2+=i
print(s1,s2**2)
if s1>s2**2:
    print("a)S1>S2")
elif s1<s2**2:
    print("a)S1<S2")
elif s1==s2**2:
    print("a)S1=S2")

for e in range(1,n+1):
    s3+=e**2
    a+=e
    s4=n**3+n**2+a
print(s3,s4)
if s3>s4:
    print("b)S1>S2")
elif s3<s4:
    print("b)S1<S2")
elif s3==s4:
    print("b)S1=S2")
