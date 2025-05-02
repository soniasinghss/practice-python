#dictionary: key value pairs, unordered, mutable
mydict={"name,":"Max","age":28,"city":"New York"}
print(mydict)
value =mydict["age"]
print(value)
mydict["email"]="max@xyz.com"
print(mydict)
del mydict["name"] #or can use mydict.pop("name") to delete name from dict
print(mydict)

if "lastname" in mydict:
    print(mydict["lastname"])