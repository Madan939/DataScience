# class Student:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"{self.name}"
# obj=Student("Madan")
# print(obj)

# Task: Create a reset password method that changes the encapsulated attribute "password"
class Credential:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    def resetPassword(self,newpassword):
        if self.__password!=newpassword:
            self.__password=newpassword
            print("Password changed successfully.")
        else:
            print("Same old password")
        
username=input("Enter name: ")
password=input("Enter password: ")
obj=Credential(username,password)
newpassword=input("Enter new password")
obj.resetPassword(newpassword)

    