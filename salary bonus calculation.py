grade=input("enter the grade of the employee:")
b=int(input("enter the employee salary:"))
if(grade=="a"):
    bonus=b/5
    print("bonus",bonus)
elif(grade=="b"):
    bonus=b/10
    print("bonus",bonus)
else:
    bonus=bonus
salary=bonus+b
print("grade is:",grade)
print("salary is:",salary)

