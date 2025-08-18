# typecasting
# print(int("56"))
# print(float("4.55"))
# print(int(2.22))

#data type
# print(type(123))
# print(type("Hello"))
# print(type(2.44))
# print(type(False))
# name=["abc","123"]
# print(type(name))

#mutable and non-mutable
#Those data type that can change it's value programatically is mutable,and by creating new objecta we can change data is non-mutable
#List = list is a data type in python that can store multiple values of different data type.
# even we can store another list inside list
# we use [] to define a list
#example
fruits=["Mango","Orange","Guava","Pineapple","Lemon","Water-melon"]
print(fruits)
fruits.append("Papaya")
print(fruits)
print(fruits.count("Mango"))
print(fruits.index("Guava"))
fruits.remove("Guava")
fruits.pop(1)
print(fruits)
#index
#positive index
print(fruits[2])#get value from index
print(fruits[0:2])#get value from start to end
print(fruits[:3])#get value from end
print(fruits[2:])#get value from start
print(fruits[::2])# index with steps
# negative index
print(fruits[-1])# get value with negative index
print(fruits[-3:-1])
print(fruits[:-2])
print(fruits[-2:])