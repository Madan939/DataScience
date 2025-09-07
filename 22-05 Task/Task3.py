# Write a python function that accepts a string and returns the string with vowels removed
vowels="aeiouAEIOU"
def vowelRemover(inp):
    word_without_vowel=""
    for x in inp:
        if x not in vowels:
            word_without_vowel+=x
    print(f"The word without vowels are {word_without_vowel}")
            
    
user_inp=input("Enter any string: ")
vowelRemover(user_inp)