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

a=(1,2,3,4,5,6,7,8,9,10)
b=a[2:5]
print(b)

my_tuple=(0,1,2,3,4)
i1,*i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)
