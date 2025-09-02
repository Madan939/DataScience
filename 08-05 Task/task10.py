# Write a function to reverse a string without using built-in functions like [::-1] or reversed().
user_input=input("Enter any string: ")
rev=""
i=len(user_input)-1
while i>=0:
    rev+=(user_input[i])
    i-=1
print(f"The reverse string of {user_input} is {rev}")