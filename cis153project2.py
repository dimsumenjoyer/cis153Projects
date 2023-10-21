'''
Victor Van 00319912
CIS153: Project 1
Professor Penta
10/16/2023, Due: 11/1/2023
'''

import random

#users_file = open("users.md", "w+")
#log_file = open("log.md", "w+")

def last_name():
    last_name = input("What is your surname?: ")
    return last_name 

def first_name():
    first_name = input("What is your given name?: ")
    return first_name

def generate_username():
    random_number = random.randint(1000,9999)
    given_name = first_name()
    surname = last_name()
    username = given_name[0] + surname + str(random_number)
    username_lower = username.lower()
    return username_lower

def getuserpassword():
    username = generate_username()
    users_file = open("users.md", "r+")
    user_file_data = users_file.read()
    if username in user_file_data:
        password = input("Create a password: ")
    else:
        print("Error: User does not exist.")
        return password

def validatepassword():
    password = getuserpassword()
    special_characters = ["!", "@", "$", "?"] 
    if special_characters in password:
        print("Error: Passwords cannot contain special characters: !, @, $, ?.")
    password_length = len(password)
    elif password_length < 5:
        print(f"Error: Passwords must be 5 characters long. This password is only {password_length} long.")
    elif password_length <= 5 and special_characters not in password:
        print(f"Error: Passwords must be 5 characters long. This password is only {password_length} long and have no special characters: !, @, $, ?.")
    else:
        unencrypted_password = getuserpassword()
    return unencrypted_password

def encryptpassword(unencrypted_password):
    encrypted_password = unencrypted_password
    encrypted_password = encrypted_password.replace("i", "!").replace("a", "@").replace("S", "$").replace("J", "?")
    return encrypted_password

def login_existing_user():
    done = False
    while not done:
        
    username_login = generate_username()
    return
'''
def review_log():
    open_logfile = open("log_file")
    for x in log_file:
        print(x)
    open_logfile.close()
    return   

def menu():
    print("Options: \n1) Login,\n2)Create Account,\n3)Review Log")
    try:
        user_input = int(input(("Choose an option: ")))
        done = False
        while not done:
            existing_user = login_existing_user()
            open_review_log = review_log()
            if user_input == "done":
                done = True
                break
            if user_input != [1,2,3] #1 and user_input != 2 and user_input != 3:
                print("Error: Invalid input. Please try again.")
    except ValueError:
            print("Error: Invalid input. Please try again.")
    return
'''