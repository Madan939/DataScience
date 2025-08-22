# Task. 12 :Calculator using methods
def calculator(num1,num2,operator):
    if operator=="+":
        return print(f"Addition={num1+num2}")
    elif operator=="-":
        return print(f"Subtraction={num1-num2}")
    elif operator=="*":
        return print(f"Multiplication={num1*num2}")
    elif operator=="/":
        return print(f"Division={num1/num2}")
    else:
        return print(f"Modulus={num1%num2}")
    
while True:
    user_input=int(input("Enter\n1. For addition\n2. For subtraction\n3. For Multiplication\n4. For Division\n5. For Modulus\n6. For exiting\n"))
    if(user_input==6):
        print("Existing...")
        break
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    match user_input:
        case 1:
            calculator(num1,num2,"+")
        case 2:
            calculator(num1,num2,"-")
        case 3:
            calculator(num1,num2,"*")
        case 4:
            calculator(num1,num2,"/")
        case 5:
            calculator(num1,num2,"%")
        case _:
            print("invalid input")