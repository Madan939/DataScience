# Write a function to check whether a given number is prime or not
def primeNumber(num):
    if num>1:
        i=2
        while i<num:
            if num%i==0:
                print(f"{num} is not a prime number.")
                break
            i+=1
        else:
            print(f"{num} is a prime number")
    else:
        print("1 is not a prime number.")
num=int(input("Enter any number: "))
primeNumber(num)
