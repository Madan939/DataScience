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
# name=["Ram","Shyam","Hari","Madan"]
# password=["sksjbsuuwef","jskdncjbsc","sdjncduu","8ehduhedd"]
# user=input("Enter your name:")
# if user in name:
#     print(f"{user} is in the list")
# else:
#     print(f"{user} not found")

# Task.8: Create a dictionary of usernames and passwords, extract all the usernames from the dictionary and input username from the user and check if the username is present in the extracted list of usernames
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
# if name in credentials.keys():
#     print(f"{name} is in the list")
# else:
#     print(f"{name} is not in the list")
#Simple calculator
# num_1=float(input("Enter first number: "))
# num_2=float(input("Enter second number: "))
# operator=input("Enter operator: ")

#using if,elif,else
# if operator=="+":
#     print("Addition= "+num_1+num_2)
# elif operator=="-":
#     print("Subtraction= "+num_1-num_2)
# elif operator=="*":
#     print("Multiplication= "+num_1*num_2)
# elif operator=="/":
#     print("Division= "+num_1/num_2)
# elif operator=="%":
#     print("Modulus= "+num_1%num_2)
# else:
#     print("operators didnot match:")
    
#using match
# match operator:
#     case "+":
#         print("Addition= "+num_1+num_2)
#     case "-":
#         print("Subtraction= "+num_1-num_2)
#     case "*":
#         print("Multiplication= "+num_1*num_2)
#     case "/":
#         print("Division= "+num_1/num_2)
#     case "%":
#         print("Modulus= "+num_1%num_2)
#     case _:
#         print("operator not found")
        
# Task : Make login and register system
credentials={
    "Ram":"ram123",
    "Shyam":"shyam123"
}
user_input=int(input("Enter: 1 for login, 2. for register"))

match user_input:
    case 1:
        username=input("Enter user name:")
        password=input("Enter password: ")
        if username in credentials and credentials.get(username)==password:
            print("Login successfully")
        else:
            print("login failed")
    case 2:
        username=input("Enter user name: ")
        password=input("Enter password: ")
        credentials.update({username:password})
        print("registered successfully")
    case _:
        print("input didnot match")