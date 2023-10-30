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

def exist_in_users(string):
    with open("users.md", "r") as file:
        if string in file:
            return True
        else:
            return False

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
    
def correct_password(username, encrypted_password):
    input_password = input("Enter your password: ")
    with open("users.md", "a+") as users_file:
        if input_password.replace("i", "!").replace("a", "@").replace("S", "$").replace("J", "?") == encrypted_password in users_file:
            print(f"Welcome {username}!")
            return True
        else:
            print("Error: Incorrect password.")
            return False

def password_handling(username):
    encrypted_password = "{Cat meme} Sexy people (ME) suffer the most."
    done = False
    while not done:
        password = create_password(username)
        if validatepassword(username, password):
            encrypted_password = encryptpassword(password)
            write_to_review_log(f"{username} created a password.\n")
            done = True
    return encrypted_password

def create_account():
    username = f"{generate_username()}\n"
    write_to_user_file(username)
    write_to_review_log(f"{username} has created an account.\n")
    print(f"Welcome {username}!")
    password = password_handling(username)
    write_to_user_file(f"{password}\n\n")
    return

def login():
    with open("users.md", "r") as file:
        inputed_username = input("username: ")
        inputed_password = input("password: ")
        if exist_in_users(inputed_username) and exist_in_users(inputed_password):
            print("Login successful!")
            done = True
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
