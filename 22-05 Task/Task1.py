# Write a program to take a string input and count the number of vowels and consonants.
user_input=input("Enter any string: ")
vowel_count=0
consonant_count=0
vowel="aeiou"
for x in user_input.lower():
    if x in vowel:
        vowel_count+=1
    if x not in vowel:
        consonant_count+=1
        
print(f"The number of vowels in {user_input} is {vowel_count}")
print(f"The number of consonants in {user_input} is {consonant_count}")
        
    
