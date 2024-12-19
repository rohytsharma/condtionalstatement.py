login_username = input("Enter your username: \n")
login_password= input("Enter your password: \n")
if login_username == "admin" and login_password == "password123":
    print("ACCESS GRANTED")
else:
    print("\nWrong username and password combination.\n ACCESS DENIED")