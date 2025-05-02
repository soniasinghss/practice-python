#tuples are ordered immutable and allow duplicates 

mytuple = "Max", 28, "Boston"
print(mytuple)
print(type(mytuple))

item=mytuple[0]
print(item)
for i in mytuple:
    print(i)
    if "Max" in mytuple:
        print("Max is in the tuple")
    else:
        print("Max is not in the tuple")
 
my_tuple=('a', 'b', 'c', 'd')
print(my_tuple.count('a'))
print(my_tuple.index('p'))
