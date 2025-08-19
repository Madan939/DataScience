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
#fruits=["Mango","Orange","Guava","Pineapple","Lemon","Water-melon"]
#print(fruits)
#fruits.append("Papaya")
#print(fruits)
#print(fruits.count("Mango"))
#print(fruits.index("Guava"))
#fruits.remove("Guava")
#fruits.pop(1)
#print(fruits)
#index
#positive index
#print(fruits[2])#get value from index
#print(fruits[0:2])#get value from start to end
#print(fruits[:3])#get value from end
#print(fruits[2:])#get value from start
#print(fruits[::2])# index with steps
# negative index
#print(fruits[-1])# get value with negative index
# print(fruits[-3:-1])
# print(fruits[:-2])
# print(fruits[-2:])
 # Tuple: Tuple is a immutable data type that wraps the element in ()
# num=(1,2,3,4,5,6)
# print(num.count(4))
# print(num[3])
# name=["a","b"]
# tup=tuple(name)
# print(tup)
# print(type(tup))

# Set
# name={"Ram","Shyam","Hari","Geeta"}
# print(name)
# name.add("Sita")
# print(name)
# name.remove("Ram")
# print(name)
# classes={1,2,4}
# unions=name | classes
# print(unions)
# name.update(unions)
# print(name)
# unions.clear()
# print(unions)
# num1={1,2,3,4,5,6}
# num2={3,4,6,7,8,9}
# print(num1.difference(num2))
# print(num1.intersection(num2))
# num1.add(8)
# num1.remove(4)
# num1.pop()
# print(num1)
# Dictionary
# car={
#     "Founder":"Abc",
#     "Industry":"Automobiles",
#     "Brand":"Toyata",
#     "Date":2055
# }
# print(car)
#access the items
# print(car["date"])
#change the value
# car["brand"]="Tesla"
# print(car)
#after adding
# car["color"]="red"
# print(car)
#remove item
# car.pop("date")
# print(car)
#print keys only
# for x in car.keys():
#     print(x)
#print values only
# for y in car.values():
#     print(y)
#using get methods
# print(car.get("color"))
#using update methods
# car.update({"color":"White"})
# print(car)
# use copy and clear the dictionary
# newCar=car.copy()
# car.clear()
# print(car)
# print(newCar)
#use popitem method
# newCar.popitem()
# print(newCar)
# for x,y in newCar.items():
#     print(f"{x} = {y}")
