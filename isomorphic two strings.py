def isIsomorphic(str1,str2):
    dist_str1 ={}
    dist_str2 ={}
    for i, values in enumerate(str1):
        dist_str1[values] = dist_str1.get(values,[])+[i]

    for j, values in enumerate(str2):

        dist_str2[values] = dist_str2.get(values,[])+[j]

    if sorted(dist_str1.values())==sorted(dist_str2.values()):
        return True
    else:
        return False

print(isIsomorphic("foo","bar"));
print(isIsomorphic("egg","add"));
print(isIsomorphic("title","paper"));
print(isIsomorphic("apple","orange"));

