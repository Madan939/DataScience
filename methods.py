# function
# def myClass():
#     print("This is function")
# myClass() 



# Table creation using methods and loops

# def table(num):
#     i=0
#     while i<=9:
#         mul=i+1
#         print(f"{num} * {mul} = {num*mul}")
#         i+=1
# while True:
#     number_input=int(input("Enter:\n1. For table\n2. For Exit\n"))
#     if number_input==2:
#         print("Existing...")
#         break
#     num=int(input("Enter the number that you want to create table:"))
#     match number_input:
#         case 1:
#             table(num)
#         case _:
#             print("invalid input...")
# functions types:
#1. Built-in functions
#2. User defined functions

#lambda function
# x=lambda a,b:a*b
# print (x(5,3))

#list comprehension
list1=[1,2,3,4,5]
list2=[x for x in range(1,7)]
print(list1)
print(list2)

#map function
numbers=[1,2,3,4,5]
sq=list(map(lambda x: x+2,numbers))
print(sq)

#filter function
num=[x for x in range(1,20)]
print(num)
even_num=list(filter(lambda x: x%2==0,num))
print(even_num)

#reduce function
from functools import reduce
num=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,num)
print(sum)

#zip function
names=["name_1","name_2","name_3"]
scores=[77,88,85]
combined=list(zip(names,scores))
print(combined)