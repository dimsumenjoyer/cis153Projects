'''
Victor Van 00319912
CIS153: Project 1
Professor Penta
10/16/2023, Due: 11/1/2023
'''

import random

#users_file = open("users.md", "w+")
#log_file = open("log.md", "w+")

def generate_username(first_name, last_name):
    random_number = random.randint(1000,9999)
    username = first_name[0] + last_name + str(random_number)
    # add create_username into user_file
    #open("users_file", "a+")
    username_lower = username.lower()
    return username_lower

#print(generate_username("Victor", "Van"))
#print(generate_username("John", "Doe"))
#print(generate_username("Jane", "Doe"))

def getuserpassword():
    username = generate_username()
    users_file = open("users.md", "r+")
    user_file_data = users_file.read()
    if username in user_file_data:
        password = input("Create a password: ")
        return password

def validatepassword():
    password = getuserpassword()
    if "!", "@", "$", or "?" in password:
        print("Passwords cannot contain special characters: !, @, $, ?.")
    password_length = len(password)
    getuserpassword()
    if password_length < 5:
    print(f"Passwords must be 5 characters long. This password is only {password_length} long.")
    #getuserpassword()
    if password_length <= 5 and "!", "@", "$", and "?" not in password:
        unencrypted_password = getuserpassword()
    return unencrypted_password

'''
def encryptpassword(unencrypted_password):
    for
    return encrypted_password

def login_existing_user():
    username_login = generate_username()
    return

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