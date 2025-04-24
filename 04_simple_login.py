import sys

username = "admin"
password = "admin"

def login():
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")
    if entered_username and entered_password:
        return entered_username, entered_password
    else:
        print("Must enter both username and password!")

def check_credentials(entered_username, entered_password):
    attempts = 0
    while True:
        attempts = attempts + 1
        if attempts == 3:
            print("Too many failed attempts, shutting off...")
            sys.exit()
        if username == entered_username and password == entered_password:
            print("Successfully Logged In!")
            change_pass()
            break
        else:
            print("Incorrect username or password, please try again!")
            entered_username, entered_password = login()

def change_pass():
    print("Please change your password for your safety: ")
    new_pass = input()
    global password
    password = new_pass
    print("-"*20)
    print("Password Changed Successfully")

usr, pss = login()
check_credentials(usr,pss)