#Write a python program that appends user input to the file until the user types exit.
def inputFile(user_inp):
    file= open("user.txt", "a")
    file.write(user_inp + ",") 
    file.close()

while True:
    user_inp = input("Enter any text: ") 
    if user_inp.lower() == "exit":
        break
    inputFile(user_inp)

