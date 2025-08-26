# Write 10 hobbies in the file with a seperator.Ask user about their hobby
# print hobby found if hobby is in file else print hobby not found
import os
hobbies=['cricket','drawing','coding','footbal','reading','singing','dancing','driving','running','swimming']
file="file.txt"
separator=","
if not os.path.exists(file):
    with open(file,"w") as f:
        f.write(separator.join(hobbies))
    print(f"{file} created successfully and data is inserted.")

with open(file,"r") as f:
        hobby_list=f.read()
        hobby=input("Enter your hobby: ")
        if hobby.lower() in hobby_list.lower():
            print(f"{hobby.capitalize()} hobby found.")
        else:
            print(f"{hobby.capitalize()} hobby not found.")
        
            
    