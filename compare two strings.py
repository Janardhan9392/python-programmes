a=input("enter S1=")
b=input("enter S2=")
c=min(len(a),len(b))
d=0
for i in range(c):
    if(a[i]==b[i]):
        d=d+1
    print(d)

