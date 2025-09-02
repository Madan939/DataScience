# Write a program to print all numbers from 1 to 50 that are divisible by 5.
num=[x for x in range(1,51)]
divisible_by_5_number=list(filter(lambda x:x%5==0,num))
print("The number that are divisible by 5 from 1 to 50 are: ")
for x in divisible_by_5_number:
    print(x)