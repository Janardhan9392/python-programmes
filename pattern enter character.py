ch=input("enter the characer:")
a=int(input("enter the number:"))
if(a>0):
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(ch,end=" ")
        print()
else:
    print("invalid:")
print()
