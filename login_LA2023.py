import hashlib
import csv
import pandas as pd
def signup(email, username, password, confirm_pass):
    if confirm_pass == password:
        enc = confirm_pass.encode()
        hashpass = hashlib.md5(enc).hexdigest()
        with open("logins.csv", newline="", mode = "a") as loginfile:
            login_writer = csv.writer(loginfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            login_writer.writerow([email, hashpass, username])
        print("Thank you for registering with Roam")
    else:
        print("Passwords do not match")
    

if __name__ == "__main__":
    email = input("Enter email: ")
    username = input("Enter a username: ")
    password = input("Enter password: ")
    confirm_pass = input("Please confirm password: ")
    signup(email, username, password, confirm_pass)


def subscribe_email(subscribe):
    if subscribe == "yes" or subscribe == "Yes" or subscribe == "YES":
        email_sub = input("What email would you like to subscribe with? ")
        subscribe = True
        with open("subscriptions.csv", newline = '', mode = 'a') as subscribefile:
            subscribe_writer = csv.writer(subscribefile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            subscribe_writer.writerow([email_sub])
        print("Thank you for subscribing!")
    elif subscribe == "no" or subscribe == "No" or subscribe == "No":
        subscribe = False
    else:
        print("Invalid input")

if __name__ == "__main__":
    subscribe = input("Would you like to subscribe? yes/no ")
    subscribe_email(subscribe)

def login(username, email, password):
    authenticate = password.encode()
    auth_hash = hashlib.md5(authenticate).hexdigest()
    user_pass = [email, auth_hash, username]
    with open("logins.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if row == user_pass:
                login1 = True
                
            else: 
                login1 = False
        if login1 == True:
            print("Welcome")
        elif login1 == False:
            print("Wrong password or email")

        #, user_username, user_password = loginfile.read().split(",")
    #user email and password refers to the saved ones tied to the user


    #if email == user_email and password == user_password:
       # print("Login successful")
        # line of code to load main page here

    #else:
        #print("Wrong password or email")

if __name__ == "__main__":
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    login(username, email, password)