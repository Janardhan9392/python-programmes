a=[]
b=int(input("enter the elements:"))
try:
    for i in range(b):
        d=int(input("enter the numbers:"))
        if(d<0):
            print("enter the positive number:")
        else:
            a.append(d)
    p=0
    c=0
    for i in a:
            if(i%2==0):
                c=c+1
            else:
                p=p+1
    print("composite",c)
    print("prime",p)

except ValueError:
    print("enter the positive number:")
