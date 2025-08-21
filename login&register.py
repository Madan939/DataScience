# Task. 11: Update login & register system using loop
data={
    "user_1":"user1pass",
    "user_2":"user2pass"
}
while True:
    user_input=int(input("Enter:\n1. For Login\n2. For Register\n3. For Exit\n"))
    if user_input==3:
        print("Existing From the System...")
        break
    username=input("Enter username: ")
    password=input("Enter password: ")
    match user_input:
        case 1:
            if username in data:
                if data.get(username)==password:
                    print("Login successfully...")
                    while True:                        
                        new_input=int(input("Enter:\n1. For editing username only \n2. For editing password only\n3. For editing both username and password\n4. For Logout\n"))
                        if new_input==4:
                            print("Logging out from System...")
                            break
                        match new_input:
                            case 1:
                                new_username=input("Enter new username: ")
                                if new_username in data:
                                    print("This username is already taken.")
                                elif new_username==username:
                                    print("Same username")
                                else:
                                    data[new_username]=data.pop(username)
                                    print(f"{username} changed into {new_username} successfully...")
                                    username=new_username
                            case 2:
                                new_password=input("Enter new password: ")
                                if new_password==password:
                                    print("Same old password")
                                else:
                                    data[username]=new_password
                                    print("password changed successfully...")
                                    password=new_password
                            case 3:
                                new_username=input("Enter new username: ")
                                new_password=input("Enter new password: ")
                                if new_username in data:
                                    print("This username is already taken.")
                                elif new_username==username:
                                    print("Same username")
                                elif new_password==password:
                                    print("Same old password")
                                else:
                                    data[new_username]=new_password
                                    data.pop(username)
                                    print("username and password changed successfully...")
                                    username,password=new_username,new_password
                                    
                            case _:
                                print("Invalid input...")
                else:
                    print("password didnot match")
            else:
                print("User not found")
        case 2:
            if username in data:
                print("User already exists...")
            else:
                data[username]=password
                print(f"user {username} registered successfully...")
        case _:
            print("Invalid input...")
            
