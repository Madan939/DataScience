# Write a program to count how many vowels are present in a given string.
user_input=input("Enter any string: ")
count=0
vowel="aeiou"
for x in user_input.lower():
    if x in vowel:
        count+=1
print(f"The number of vowels in {user_input} is {count}")
        
    
