'''
Victor Van 00319912
CIS153: Project 2 
Professor Penta
10/16/2023, Due: 11/1/2023
'''

import random

def write_to_user_file(user_info):
    with open("users.md", "a+") as users_file:
        users_file.write(user_info)
    return

def write_to_review_log(message):
    with open("log_file.md", "a+") as log_file:
        log_file.write(message)
    return

def display_review_log():
    with open("log_file.md", "r") as log_file:
        print(log_file.read())
    return

def generate_username():
    random_number = random.randint(1000, 9999)
    given_name = input("What is your given name?: ")
    surname = input("What is your surname?: ")
    inputed_username = given_name[0] + surname + str(random_number)
    username = inputed_username.lower()
    return username 

def exist_in_users(user):
    wordpass = None
    with open("users.md", "r") as file:
        for line in file:
            line.startswith(user)
            index = line.find("::")
            if line.startswith(user):
                wordpass = line[index+2:].strip()
    return wordpass

def create_password(username):
    with open("users.md", "r") as file:
        if username in file:
            password = input("Create a password: ")
            return password
        else:
            print("Error: User does not exist. Make a user.")
            return

def special_character_check(password):
    if "!" in password or "@" in password or "$" in password or "?" in password:
        print("Error: Passwords cannot contain special characters: !, @, $, ?.")
        return True
    else:
        return False

def validatepassword(username, password):
    password_length = len(password)
    has_special_character = special_character_check(password)
    if password_length < 5 and has_special_character:
        print(f"Error: Passwords must be 5 characters long. This password is {password_length} long and contains special characters: !, @, $, ?.")
        write_to_review_log(f"Bad Password - FAIL - {username}.\n")
        return False
    elif password_length < 5:
        print(f"Error: Passwords must be 5 or more characters long. This password is only {password_length} long.")
        write_to_review_log(f"Bad Password - FAIL - {username}.\n")
        return False
    elif has_special_character:
        print("Error: This password has special characters: !, @, $, ?")
        return False
    else:
        write_to_review_log(f"{username} created a password.\n")
        return True

def encryptpassword(password):
    encrypted_password = password.replace("i", "!").replace("a", "@").replace("S", "$").replace("J", "?")
    return encrypted_password
    
def correct_password(username, inputed_password):
    file_password = exist_in_users(username)
    if file_password is not None:
        encrypted_input_password = encryptpassword(inputed_password)
        if encrypted_input_password == file_password:
            print(f"Welcome {username}!")
            return True
    print("Error: Incorrect password.")
    return False
        
def password_handling(username):
    encrypted_password = "{Cat meme} Sexy people (ME) suffer the most."
    password = input("Create a password: ")
    while not validatepassword(username, password):
        password = input("Create a password: ")
    encrypted_password = encryptpassword(password)
    write_to_user_file(f"{username}::{encrypted_password}\n")
    return encrypted_password

def create_account():
    username = generate_username()
    password_handling(username)
    print(f"Welcome {username}!")
    write_to_review_log(f"{username} has created an account.\n")
    return

def login():
    inputed_username = input("username: ")
    inputed_password = input("password: ")
    file_password = exist_in_users(inputed_username)
    if not file_password == None:
        encrypted_password = encryptpassword(inputed_password)
        if encrypted_password == file_password:
            print("Login successful!")
            write_to_review_log(f"{inputed_username} logged in.\n")
        else:
            print("Error: Login unsuccessful!")
    else:
        print("Error: Login unsuccessful.")
        write_to_review_log(f"Login attempt failed: {inputed_username}.\n")
    return

def menu():
    option = 0
    done = False
    while not done:
        print("Options:\n1) Login\n2) Create Account\n3) Review Log\n4) Exit")
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                login()
            elif option == 2:
                create_account()
            elif option == 3:
                print("REVIEW LOG:\n")
                display_review_log()
            elif option == 4:
                print("Exited.")
                done = True
            else:
                print(f"Error: Invalid input: {option}. \nPlease try again.")
        except ValueError:
            print(f"Error: Invalid input: {option}.\nPlease try again.")
    return

menu()