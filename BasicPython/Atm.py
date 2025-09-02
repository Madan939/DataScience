import json
import os

file_name = "Atmdata.txt"
def register(username, pin):
    print("Register:")
    credential = {
        "username": username,
        "pin": pin,
        "balance": 0
    }
    if not os.path.exists(file_name):
        data = [credential]
        file = open(file_name, "w")
        file.write(json.dumps(data)) 
        file.close()
        print("Registered successfully.")
        return
    file = open(file_name, "r")
    content = file.read()
    file.close()
    if content.strip() == "":
        data = []
    else:
        data = json.loads(content)
    for i in data:
        if i["username"] == username:
            print("Username already exists.")
            return
    data.append(credential)
    file = open(file_name, "w")
    file.write(json.dumps(data))
    file.close()
    print("Registered successfully.")

def login(username,pin_code):
    if not os.path.exists(file_name):
        print("File not found")
        return
    else:
        file = open(file_name, "r")
        content = file.read()
        file.close()
        if content.strip() == "":
            data = []
        else:
            data = json.loads(content)
        for i in data:
            if i!="":
                if i["username"] == username and i["pin"]==pin_code:
                    print("Login successfull.")
                    balance=i["balance"]
                    while True:
                        user_input=int(input("Enter:\n1.Check balance \n2.Add balance\n3.Widthdrawl\n4Logout\n: "))
                        if user_input==4:
                            file = open(file_name, "w")
                            file.write(json.dumps(data))
                            file.close()
                            print("User logout from ATM Machine")
                            break
                        match user_input:
                            case 1:
                                print(f"Your balance is Rs.{balance}")
                            case 2:
                                add_balance=int(input("Enter the amount: "))
                                balance+=add_balance
                                i["balance"]+=add_balance
                                print(f"Rs.{add_balance} added successfully")
                            case 3:
                                widthdrawl=int(input("Enter the amount: "))
                                if widthdrawl%500==0:
                                    if widthdrawl>balance:
                                        print("insufficient balance")                                    
                                    elif widthdrawl>25000:
                                        print("You can widthdrawl only Rs.25000 at a time")                                    
                                    else:
                                        balance-=widthdrawl
                                        i["balance"]-=widthdrawl
                                        print(f"Rs.{widthdrawl} widthdrawl successfully.")
                                else:
                                    print("Balance should be divisible by Rs.500")
                            case _:
                                print("Invalid input")
                    break
        else:
            print("Login failed")                            
            
while True:
    choice = int(input("Enter\n1. For Register\n2. For Login\n3. For Exit\n: "))
    if choice == 3:
        print("Exiting from ATM Machine...")
        break  
    username = input("Enter username: ")
    pin_code = int(input("Enter four digits pin code: "))
    match choice:
        case 1:
            register(username,pin_code)
        case 2:
            login(username,pin_code)
        case _:
            print("Invalid input")
            
