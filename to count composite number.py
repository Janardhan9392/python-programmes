a=int(input("Enter start range:"))
b=int(input("Enter end range:"))
if(a>b or a==0 or b==0):
    print("INVALID INPUT")
elif(a>0 or b<0):
     print("Composite number from",a,"to",b)
for i in range(a+2,b):
    for j in range(2,a):
        if(i%j==0):
            print(i)
            break
else:
    print(i)
