# calculator with exception handling
def add(num1,num2):
    print(f"Addition: {num1+num2}")
def sub(num1,num2):
    print(f"Subtraction: {num1-num2}")
def mul(num1,num2):
    print(f"Multiplication: {num1*num2}")
def div(num1,num2):
    try:
        print(f"Division: {num1/num2}")
    except ZeroDivisionError as e:
        print(e)
def mod(num1,num2):
    try:
        print(f"Modulus: {num1%num2}")
    except ZeroDivisionError as e:
        print(e)
while True:
    try:
        choice=int(input("Enter:\n1.For Addition\n2.For Subtraction\n3.For Division\n4.For Multiplication\n5.For Modulus\n6.For Exit\n:"))
        if choice==6:
            print("Exiting...")
            break
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        match choice:
            case 1:
                add(num1,num2)
            case 2:
                sub(num1,num2)
            case 3:
                div(num1,num2)
            case 4:
                mul(num1,num2)
            case 5:
                mod(num1,num2)
            case _:
                print("Invalid input")                
    except ValueError as e:
        print(e)