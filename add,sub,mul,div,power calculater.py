def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b
def devision(a,b):
    return a/b
def power(a,b):
    return a**b
print("enter the choice:")
print("1.add")
print("2.subtract")
print("3.mul")
print("4.division")
print("5.power")

choice=int(input("please enter the 1/2/3/4/5:"))
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))


if(choice==1):
    print(num1,"+",num2,num1+num2)
elif(choice==2):
    print(num1,"-",num2,num1-num2)
elif(choice==3):
    print(num1,"*",num2,num1*num2)
elif(choice==4):
    print(num1,"/",num2,num1/num2)
elif(choice==5):
    print(num1,"**",num2,num1**num2)
else:
    print("invalid")
