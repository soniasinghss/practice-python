

list_org=["banana","cherry","apple"]
list_cpy=list_org
list_cpy=list_org[:] #slicing like this will also make a copy
list_cpy.append("lemon") #same list in memory so changes to cpy are reflected in org as well

print(list_cpy)
print(list_org)

mylist=[1,2,3,4,5,6]
b=[i*i for i in mylist]
print(mylist)
print(b)