# Task 1. WAP to print your name
# print("Madan Golay Tamang")
# Task 2. Input a Favourite player and print it's name
#name=input("Enter your favourite player name: ")
#print(name)
# Task 3. Input for every data type and print it

#num=int(input("Enter any integer: "))#integer
#name=input("Enter any string: ")# string
#float_num=float(input("Enter any floating number: ")) # string

#print type 
#print(type(num))
#print(type(name))
#print(type(float_num))

#print all
#print(f"Integer= {num}, String= {name}, float= {float_num}")

# Task 4. Ask input of two numbers from the user and perform operations on those numbers or values
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# Operations
# print(num1+num2)
# print(num1==num2)
# print(num1%num2)
# print(num1>num2)
# print(num1**3)
# print(num1*num2)
# print(num1/num2)
# print(num1//num2)
# print(num1==5 and num2!=3)
# print(num1==5 or num2<4)
# num2+=num1
# print(num2)

# Task 5. Ask user a string and print if b is in that string or not. Do use in and not in

# name=input("Enter your name: ")
# if "b" in name:
#     print("b is present")
# elif "b" not in name:
#     print("b is absent by not in method")
# else:
#     print("b is absent")



#Task: 6. Implement all the indexing and slicing in string 
# name="mindrisers institute"
# print(name)
# print(name.capitalize())
# print(name.upper())
# print(name.strip())
# print(name.replace("m","M"))
# print(name.split(" "))

# print(name[0])

#positive index
# print(name[0:4])
# print(name[:5])
# print(name[4:])

#negative index
# print(name[-1])
# print(name[:-3])
# print(name[-2:])
# print(name[-4:-1])

# Task.7: Get input from user and check if user name is in the list or not
# name_list=["Ram","Shyam","Hari","Madan"]
# user=input("Enter your name:")
# if user in name_list:
#     print(f"{user} is in the list")
# else:
#     print(f"{user} not found")

# Task 8: Create a dictionary of usernames and passwords, extract all the usernames from the dictionary and input username from the user and check if the username is present in the extracted list of usernames
# credentials={
#     "Ram":"ramabc",
#     "Shyam":"shyamabc",
#     "Hari":"hariabc"
# }
#print all username
# for x in credentials.keys():
#     print (x)
# check if username is present or not
# name=input("Enter the username:")
# if name in credentials:
#     print(f"{name} is in the list")
# else:
#     print(f"{name} is not in the list")

#Simple calculator
# num_1=float(input("Enter first number: "))
# num_2=float(input("Enter second number: "))
# operator=input("Enter operator: ")
# if operator=="+":
#     print(f"Addition= {num_1+num_2}")
# elif operator=="-":
#     print(f"Subtraction= {num_1-num_2}")
# elif operator=="*":
#     print(f"Multiplication= {num_1*num_2}")
# elif operator=="/":
#     print(f"Division= {num_1/num_2}")
# elif operator=="%":
#     print(f"Modulus= {num_1%num_2}")
# else:
#     print("operators didnot match:")
    
        
# Task 9 : Make login and register system
# credential={
#     "Ram":"ram123",
#     "Shyam":"shyam123"
# }
# user_input=int(input("Enter:\n 1. For login \n 2. For Register\n"))

# match user_input:
#     case 1:
#         username=input("Enter user name:")
#         password=input("Enter password: ")
#         if username in credential :
#             if credential.get(username)==password:
#                 print("Login successfully")
#             else:
#                 print("password did not match")
#         else:
#             print("username did not exist")
#     case 2:
#         username=input("Enter user name: ")
#         password=input("Enter password: ")
#         if username in credential:
#             print("Username already exits.")
#         else:
#             credential.update({username:password})
#             print(f"user {username}, registered successfully")
#     case _:
#         print("input didnot match")

# Task. 10 Create a fully functional calculator using loop
# while True:
#     user_input=int(input("Enter\n1. For addition\n2. For subtraction\n3. For Multiplication\n4. For Division\n5. For Modulus\n6. For exiting\n"))
#     if(user_input==6):
#         print("Existing...")
#         break
#     num1=int(input("enter first number:"))
#     num2=int(input("enter second number:"))
#     match user_input:
#         case 1:
#             print(f"Addition={num1+num2}")
#         case 2:         
#             print(f"Subtraction={num1-num2}")
#         case 3:
#             print(f"Multiplication={num1*num2}")
#         case 4:
#             print(f"Division={num1/num2}")
#         case 5:
#             print(f"Modulus={num1%num2}")
#         case _:
#             print("invalid input")
# print("Thank you for using our system")


