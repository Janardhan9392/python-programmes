try:
    n=input("enter the string:")
except:
    ValueError
    print("enter th proper input:")
else:
    def reverse(n):
        str1="   "
        for i in n:
            str1=i+str1
        return str1    
print("given string:",n)
print("reverse string:",reverse(n))
