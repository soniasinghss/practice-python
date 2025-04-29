x = input('name: ')
if x == 'tim':
    print('you are great!')
elif x == 'Joe':
    print('bye joe')

x = [4,True,'hi']
x.append('hello') #add hello to the list
x.extend([4,5,5,5,5,5])#adds these new elements at the end of the list
print(x.pop()) #removes last element of the list
print(x.pop(0)) #removes element at index 0 (4)
print(len(x)) #len is the length of the collection

for i in range(10):
    print(i)