'''
Victor Van 00319912
CIS153: Project 1
Professor Penta
9/25/2023, Due: 10/9/2023
'''

import random

def fortune_teller():
    question_input = input("Enter a question: ")
    print("Question: " + question_input)
    random_integer = random.randint(1, 6)

    if random_integer == 1:
        print("Answer: Yes.")
    elif random_integer == 2:
        print("Answer: No.")
    elif random_integer == 3:
        print("Answer: Maybe I might think about considering it.")
    elif random_integer == 4:
        print("Answer: Try again later.")
    elif random_integer == 5:
        print("Awswer: No chance.")
    elif random_integer == 6:
        print("Awswer: Absolutely.")

def knock_knock_joke():
    print("Knock. Knock.")
    done = False
    while not done:
        user_input = input("Response: ")
        if user_input != "Who's there?" and user_input != "Who is there?":
            print("That is not how this works.")
        elif user_input == "Who's there?" or user_input == "Who is there?":
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

def mad_lib():
  name = input("Choose a name: ")
  adjective = input("Choose an adjective: ")
  noun = input("Choose a noun: ")
  verb = input("Choose a verb: ")
  print(name + " is " + adjective + " " + noun + " and " + verb + " their friends.")

def mainmenu(menu_number):
    if menu_number == 1:
      print("FORTUNE TELLER: ")
      return fortune_teller()
    elif menu_number == 2:
      print("KNOCK KNOCK JOKE: ")
      return knock_knock_joke()
    elif menu_number == 3:
      print("MAD LIB: ")
      return mad_lib()
    else:
      print("Error: Invalid Input.")
'''
# Test
mainmenu(1)
mainmenu(2)
mainmenu(3)
mainmenu("hi")
'''

def main_menu():
  done = False
  while not done:
    print("ACTIVITY OPTIONS: \n 1) Fortune Teller \n 2) Knock Knock Joke \n 3) Mad lib")
    try:
      user_input4 = float(input("Choose a number to select your activity: "))
      if user_input4 == 1:
        print("FORTUNE TELLER: ")
        return fortune_teller()
        done = True
        break
      elif user_input4 == 2:
        print("KNOCK KNOCK JOKE: ")
        return knock_knock_joke()
        done = True
        break
      elif user_input4 == 3:
        print("MAD LIB: ")
        done = True
        break
        return mad_lib()
      else:
        print("Error: Invalid input. Please try again.")
    except ValueError:
      print("Error: Invalid input. Please try again.")
      continue

main_menu()