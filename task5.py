#Write a program to print the multiplication table of a given number.
num=int(input("Enter a number you want to find the multiplication: "))
i=0
while i<=9:
    mul=i+1
    print(f"{num} * {i+1} = {num*mul}")
    i+=1