# Authentication system using file handling and functions:
import json
import os
def register(username,password):
    data={username:password}
    if not os.path.exists("credentials.txt"):
        jsonData=json.dumps(data)
        file=open("credentials.txt","a")
        file.write(jsonData+",")
        print("Registered successfully.")
        file.close()
    else:        
        file=open("credentials.txt","r")
        content=file.read()
        file.close()
        listOfCredentials=content.split(",")
        for i in listOfCredentials:
            if i!="":
                dictI=json.loads(i)
                if username in dictI:
                    print("Username already exists.")
                    return
                else:
                    jsonData=json.dumps(data)
                    file=open("credentials.txt","a")
                    file.write(jsonData+",")
                    print("Registered successfully.")
                    file.close()
      
def login(username,password):
    file=open("credentials.txt","r")
    content=file.read()
    file.close()
    listOfCredentials=content.split(",")
    for i in listOfCredentials:
        if i!="":
            dictI=json.loads(i)
            if username in dictI and password==dictI[username] :    
                print("Login successfull.")
                break
    else:
        print("Login failed.")
# For Else=> if break found in loop, it exists the else part also. If break not found in for then else part runs

while True:
    choice=int(input("Enter\n1. For Register\n2. For Login\n3. For Exit\n: "))
    if choice==3:
        print("Exiting from the system...")
        break
    match choice:
        case 1:
            print("Register:")
            username=input("Enter username: ")
            password=input("Enter password: ")
            register(username,password)
        case 2:
            print("Login:")
            username=input("Enter username: ")
            password=input("Enter password: ")
            login(username,password)
        case _:
            print("Invalid input.")
# Task: Update this program with loops and check for duplicate username.