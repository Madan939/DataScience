#Write a program to check if a given number is even or odd.
num=int(input("Enter any number: "))
if num==0:
    print(f"{num} is zero.")
else:
    if num%2==0:
        print(f"{num} is even number.")
    else:
        print(f"{num} is odd number.")
    