# class Student:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"{self.name}"
# obj=Student("Madan")
# print(obj)

# Task: Create a reset password method that changes the encapsulated attribute "password"
# class Credential:
#     def __init__(self,username,password):
#         self.username=username
#         self.__password=password
#     def resetPassword(self,newpassword):
#         if self.__password!=newpassword:
#             self.__password=newpassword
#             print("Password changed successfully.")
#         else:
#             print("Same old password")
        
# username=input("Enter name: ")
# password=input("Enter password: ")
# obj=Credential(username,password)
# newpassword=input("Enter new password")
# obj.resetPassword(newpassword)

# Decorators=> Decorators are the special kind of function that takes another function as a argument and returns a modified version without changing the original function.
# we use @ to use decorator
# def myDecorator(func):
#     def abc():
#         print("Hello world!")
#         func()
#         print("Hello World!")
#     return abc

# @myDecorator
# def hello():
#     print("Data science")
# hello()

# static method
# class Student:
#     @staticmethod
#     def printName():
#         print("Name of the person")
# obj=Student()
# obj.printName()

#polymorphism
# class Student:
#     def __init__(self,name,password):
#         self.name=name
#         self.password=password
#     def __str__(self):
#         return f"{self.name},{self.password}"
# obj1=Student("std1","std1234")
# obj2=Student("std2","std2234")
# print(obj1)
# print(obj2)

# Abstraction
# abstract method
# ABC=Abstract Base Class
from abc import ABC,abstractmethod
class Teacher:
    @abstractmethod
    def teaches(self):
        print("I am a teacher.")
class EnglishTeacher(Teacher):
    def teaches(self):
        print("I am a english teacher.")
class MathTeacher(Teacher):
    def teaches(self):
        print("I am a math teacher.")
m1=MathTeacher()
m1.teaches()

        