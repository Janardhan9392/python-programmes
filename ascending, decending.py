n=int(input("enter the string:"))
list=[]
for i in range(n):
    c=input("enter the elements:")
    list.append(c)
list1=sorted(list)
list2=sorted(list,reverse=True)
choice=input("enter the character:")
if(choice=="a"):
    print("ascending",list1)
else:
    print("decsending",list2)
