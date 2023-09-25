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

#fortune_teller()

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
                #elif user_input2 == "Why are you crying?":
                    #done = True
                    #break
            done = True
            break

knock_knock_joke()

#def mad_lib():
'''
def main_menu():
    print("Activites:\n 1) Fortune Teller\n 2) Knock Knock Joke\n 3) mad lib")
    done = False
    while not done:
        user_input3 = input("Number a number to choose your activity: ")
        if user_input3 != "1" or user_input3 != "2" or user_input3 != "3":
            print("Error: Invalid input. Please try again")
        else:
            print("Okay!")
            done = True
            break
    done = True
    break

#main_menu()
'''