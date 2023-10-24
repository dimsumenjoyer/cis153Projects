'''
Victor Van 00319912
CIS153: Project 2 
Professor Penta
10/16/2023, Due: 11/1/2023
'''

import random

users_file = open("users.md", "w+")
log_file = open("log.md", "w+")

def last_name():
    last_name = input("What is your surname?: ")
    return last_name

def first_name():
    first_name = input("What is your given name?: ")
    last_name()
    return first_name

def generate_username():
    first_name()
    random_number = random.randint(1000, 9999)
    given_name = first_name()
    surname = last_name()
    username = given_name[0] + surname + str(random_number)
    username_lower = username.lower()
    return username_lower

def create_userpassword():
    username = generate_username()
    users_file = open("users.md", "r+")
    user_file_data = users_file.read()
    if username in user_file_data:
        password = input("Create a password: ")
        return password
    else:
        print("Error: User does not exist. Make a user.")
        return

def create_account():
    generate_username()
    create_userpassword()
    return

def has_special_character():
    password = create_userpassword()
    if "!" in password or "@" in password or "$" in password or "?" in password:
        print("Error: Passwords cannot contain special characters: !, @, $, ?.")
        return True
    else:
        return False 

def validatepassword():
    password = create_userpassword()
    password_length = len(password)
    if password_length < 5 and has_special_character():
        print(f"Error: Passwords must be 5 characters long. This password is {password_length} long and contains special characters: !, @, $, ?.")
    elif password_length < 5:
        print(f"Error: Passwords must be 5 characters long. This password is only {password_length} long.")
    elif has_special_character():
        print("Error: This password has special characters: !, @, $, ?")
    else:
        unencrypted_password = create_userpassword()
        return unencrypted_password

def encryptpassword():
    encrypted_password = validatepassword()
    encrypted_password = encrypted_password.replace("i", "!").replace("a", "@").replace("S", "$").replace("J", "?")
    return encrypted_password

def correct_password():
    input_password = input("Enter your password: ")
    if input_password == encryptpassword():
        print("Welcome!")
        return True
    else:
        print("Error: Incorrect password.")
        return False

def login_existing_user():
    done = False
    while not done:
        username_login = generate_username()
        users_file = open("users.md", "r+")
        user_file_data = users_file.read()
        if username_login in user_file_data:
            correct_password()
        else:
            print("Error: User does not exist.")
            print("FAIL.")
    return

def review_log():
    return

def display_review_log():
    logfile = open("log_file")
    for line in logfile:
        print(line)
    logfile.close()
    return   

def menu():
    print("Options:\n1) Login,\n2) Create Account,\n3) Review Log,\n4) Exit")
    try:
        user_input = int(input(("Choose an option: ")))
        done = False
        while not done:
            if user_input == 4:
                print("Done!")
                done = True
                break
            elif user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                print("Error: Invalid input. Please try again.")
            elif user_input == 1:
                print("1) Login")
                login_existing_user()
            elif user_input == 2:
                create_account()
            elif user_input == 3:
                display_review_log()
    except ValueError:
            print("Error: Invalid input. Please try again.")
    return