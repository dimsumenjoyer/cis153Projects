'''
Victor Van 00319912
CIS153: Project 2 
Professor Penta
10/16/2023, Due: 11/1/2023
'''

import random

users_file = open("users.md", "a")
log_file = open("log_file.md", "a")

def generate_username():
    random_number = random.randint(1000, 9999)
    given_name = input("What is your given name?: ")
    surname = input("What is your surname?: ")
    username = given_name[0] + surname + str(random_number)
    user_info = username.lower()
    user_file(user_info)
    review_log(f"New User - OK - {username.lower()}\n")
    return username

def create_userpassword():
    username = generate_username()
    users_file = open("users.md", "r")
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
    if generate_username() in users_file:
        user_info = generate_username() + encryptpassword()
        print("Account created!")
        user_file(user_info + "\n")
    return

def has_special_character():
    password = create_userpassword()
    if "!" in password or "@" in password or "$" in password or "?" in password:
        print("Error: Passwords cannot contain special characters: !, @, $, ?.")
        return True
    else:
        return False 

def validatepassword():
    username = generate_username()
    password = create_userpassword()
    password_length = len(password)
    if password_length < 5 and has_special_character():
        print(f"Error: Passwords must be 5 characters long. This password is {password_length} long and contains special characters: !, @, $, ?.")
        review_log("Bad Password - FAIL - " + username + "\n")
    elif password_length < 5:
        print(f"Error: Passwords must be 5 or more characters long. This password is only {password_length} long.")
        review_log("Bad Password - FAIL - " + username)
    elif has_special_character():
        print("Error: This password has special characters: !, @, $, ?")
    else:
        unencrypted_password = create_userpassword()
        review_log(f"Bad Password - FAIL - {username}\n")
        return unencrypted_password

def encryptpassword():
    encrypted_password = validatepassword()
    encrypted_password = encrypted_password.replace("i", "!").replace("a", "@").replace("S", "$").replace("J", "?")
    user_info = encrypted_password
    user_file(user_info)
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
        username = input("What is your username?: ")
        #username = generate_username()
        users_file = open("users.md", "r")
        user_file_data = users_file.read()
        if username in user_file_data:
            correct_password()
            print("Login successful.")
            review_log(f"Login successful - {username}\n")
            done = True
            break
        else:
            print("Error: User does not exist.")
            done = True
            break
    return

def user_file(user_info):
    file = open("users.md", "a+")
    file.write(user_info)
    file.close()
    return

def review_log(message):
    file = open("log_file.md", "a+")
    file.write(message)
    file.close()
    return

def display_review_log():
    logfile = open("log_file.md", "r")
    print(logfile.read())
    logfile.close()
    return

def menu():
    print("Options:\n1) Login\n2) Create Account\n3) Review Log\n4) Exit")
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
                done = True
                break
            elif user_input == 2:
                create_account()
                done = True
                break
            elif user_input == 3:
                display_review_log()
                done = True
                break
    except ValueError:
            print("Error: Invalid input. Please try again.")
    return

menu()