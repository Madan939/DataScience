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

# Simple calculator
# num_1=float(input("Enter first number: "))
# num_2=float(input("Enter second number: "))
# operator=input("Enter operator: ")
# if(operator=="+" and operator=="-" and operator=="*" and operator=="/" and operator=="%"):
#     match operator:
#         case "+":
#             print(num_1+num_2)
#         case "-":
#             print(num_1-num_2)
#         case "*":
#             print(num_1*num_2)
#         case "/":
#             print(num_1/num_2)
#         case "%":
#             print(num_1%num_2)
#         case _:
#             print("operator not found")
            
# else:
#     print("operators didnot match:")

#Task: 6. Implement all the indexing and slicing in string 
name="mindrisers institute"
print(name)
print(name.capitalize())
print(name.upper())
print(name.strip())
print(name.replace("m","M"))
print(name.split(" "))

print(name[0])

#positive index
print(name[0:4])
print(name[:5])
print(name[4:])

#negative index
print(name[-1])
print(name[:-3])
print(name[-2:])
print(name[-4:-1])