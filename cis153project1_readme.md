Victor Van 00319912
CIS153: Project 1
Professor Penta
9/25/2023, Due: 10/9/2023

# Introduction:
This is project 1 for cis153.

For this project, I have to make at least 4 functions with the following requirements:

-have a numbered menu of my 3 other functions
-the other 3 functions must be a fortune teller, a knock knock joke, and a mad lib
-at least one of the functions must be "fruitful" and at least one must a parameter(s) & return a value

# Menu Options:
I used this function to return a the user input to my main menu function.
I'm not sure if creating two seperate functions is beneficial, 
but it apparently makes my code easier to read for other people.
If the user inputs an invalid input such as an integer that's not 1-3 or
a string, then it prints out a custom error message.
I had to account for these invalid inputs seperately as invalid integers and strings.

# Fortune Teller:
I imported the random library which generates a random integer between 1-6, 
and matches that integer to strings that correlates to that integer.
To fulfill the requirements of using a definition with an argument (a parameter),
I made another function called random_integer to generate a random integer between 1 and 6.
I didn't initally understand how return statements work, but now that I do I stored that
random integer to automatically fill the parameter of my function for fortune teller.
Using a function specifically for randomly generately numbers is also a good way to reuse
that functionality. However, I would only reuse it if I wanted to generate a random number
specifically 1-6 which limits how often I would be able to use this function.
However, I believe that using dictionaries would be more efficient.
I'd just store 1-6 and their respective corresponding answers to a dictionary.
I don't understand dictionaries well enough to all those values automatically in a succint manner.
Therefore, for now, I just used a if statement to complete my function.

# Tell a Knock Knock Joke:
In this function, it prints "knock knock." If you don't answer "Who's there" and
"Who is there?", then it repeatedly prints" that's not how this works."
If you print "Who's there" or "Who is there?"

# Complete a Mad Lib:
I have 4 different variables: name, adjective, noun, and verb.
Each variable asks an input that corresponds.
Finally, it prints those variables in a predetermined sentence.

# Main Menu:
My main menu function simply takes the integer input from the main menu options function
and calls their respective functions.

# Final Thoughts:
At the moment, my python skills are not good. I think that learning how to use dictionaries to simplify things.
I also was tested my skills with composite while loops and if statements, which I thought was easy.