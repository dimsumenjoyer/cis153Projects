'''
Victor Van 00319912
CIS153: Project 1
Professor Penta
9/25/2023, Due: 10/9/2023
'''

import random

def menu_options():
  print("MENU OPTIONS: \n 1) Fortune Teller \n 2) Knock Knock Joke \n 3) Mad Lib")
  done = False
  while not done:
    try:
      user_input = int(input("Choose an activity: "))
      if user_input == 1 or user_input == 2 or user_input == 3:
        return user_input
      else:
        print("Error: Invalid Input. Please try again.")
    except ValueError:
      print("Error: Invalid Input. Please try again.")

def random_integer():
  randominteger = random.randint(1, 6)
  return randominteger

def fortune_teller(randominteger):
    input("Enter a question: ")
    randominteger = random_integer()
    print(randominteger)
    if randominteger == 1:
        print("Answer: Yes.")
    elif randominteger == 2:
        print("Answer: No.")
    elif randominteger == 3:
        print("Answer: Maybe I might think about considering it.")
    elif randominteger == 4:
        print("Answer: Try again later.")
    elif randominteger == 5:
        print("Awswer: No chance.")
    elif randominteger == 6:
        print("Awswer: Absolutely.")
    return

def knock_knock_joke():
    print("Knock. Knock.")
    done = False
    while not done:
        user_input2 = input("Response: ")
        if user_input2 != "Who's there?" and user_input2 != "Who is there?":
            print("That is not how this works.")
        elif user_input2 == "Who's there?" or user_input2 == "Who is there?":
            print("Boo - Boo. Who?")
            while not done:
                user_input2 = input("Response: ")
                if user_input2 != "Why are you crying?":
                    print("That is not how this works.")
                elif user_input2 == "Why are you crying?":
                    done = True
                    break
            done = True
            break
            return

def mad_lib():
  name = input("Choose a name: ")
  adjective = input("Choose an adjective: ")
  noun = input("Choose a noun: ")
  verb = input("Choose a verb: ")
  print(f"{name} is (a[n]) {adjective} {noun} and {verb} their friends.")
  return

def main_menu():
    user_input = menu_options()
    if user_input == 1:
      print("FORTUNE TELLER: ")
      fortune_teller(random_integer())
    elif user_input == 2:
      print("KNOCK KNOCK JOKE: ")
      knock_knock_joke()
    elif user_input == 3:
      print("MAD LIB: ")
      mad_lib()
    else:
      print("Error: Invalid Input.")
    return

main_menu()