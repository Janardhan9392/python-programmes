def reverse_string(str):
    str1=" "
    for i in str:
        str1=i+str1
    return str1
str=input("enter the string:")
print("the orginal string is:",str)
print("the reverse string is:",reverse_string(str))




