n1=int(input("enter the number1:"))
n2=int(input("enter the number2:"))
n3=int(input("enter the number3:"))


while(n1>n2) and (n1>n3):
    print("the maximum number",n1)
    break
while(n2>n1) and (n2>n3):
    print("the maximum number",n2)
    break
while(n3>n1) and (n3>n2):
    print("the maximum number",n3)
    break

