import cmath
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
d=(b**2-4*a*c)
s1=(-b-cmath.sqrt(d))/(2*a)
s2=(-b+c
    math.sqrt(d))/(2*a)
print("solution is:",s1,"and",s2)
