#Task 13. Calculator using lambda functions

add=lambda num1,num2: num1+num2
sub=lambda num1,num2:num1-num2
mul=lambda num1,num2: num1*num2
div=lambda num1,num2: num1/num2
mod=lambda num1,num2: num1%num2

while True:
    user_input=int(input("Enter\n1. For addition\n2. For subtraction\n3. For Multiplication\n4. For Division\n5. For Modulus\n6. For exiting\n"))
    if(user_input==6):
        print("Existing from system...")
        break
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    match user_input:
        case 1:
            print(add(num1,num2))
        case 2:
            print(sub(num1,num2))
        case 3:
            print(mul(num1,num2))
        case 4:
            print(div(num1,num2))
        case 5:
            print(mod(num1,num2))
        case _:
            print("invalid input")