Victor Van 00319912
CIS153: Project 2 
Professor Penta
10/25/2023, Due: 11/1/2023

With some input from Professor Walton, I rewrote my entire project basically from scatch
with more arguments in functions. I also made more functions to simplify things.
Also, it doesn't seem like writing 150 lines worth of code without testing it until the end
is a good idea.

I have 2 functions specifically for writing to files because
it was easier to work with than global variables as files.

I also made a function for display review log. I've had to break up my functions to simplify things.
I also did not use many composite loops unlike in project 1.

It's best to break down my code starting from the menu
function because all of my other functions break down from there.

# Option 3:
Option 3 prints my log file.

# Option 2:
Option 2 creates an account by calling generate_username
and stores it into a variable called username.
After that, it sends that variable to the function password_handling.
Then it asks for to create a password.
Then there's a variable that uses the password as an argument
and returns an encrypted version of it.
Then it stores the username and password in the users.md file
in the format username::password. It also returns the encrypted password as an output.

# Option 1:
Option 1 calls the function login. It prompts the user
to enter in a username and password.
Then the function exist_in_users takes the inputed_password,
search it from the file and then stores it into the variable file_password.
If the password doesn't exist in the file, then it returns None.
While file_password is not None, encrypted_password is
the password that matches inputed_password and
encrypted_password is searches for inputed_password in the users.md file.
If encrypted_password is the same as file_password, then it prints "Login successful!"

# Conclusion:
I was confused why I had to set wordpass equal to None in the function exist_in_users.
Professor Penta recommended me to do that.
Why can't I set wordpass equal to a string?
In the function password_handling, I don't really understand why I had to create a string for encrypted_password 
since it later gets defined in the while loop.
In the function menu, I don't understand why I had to set option to a integer because, later on,
option is defined as the integer of an input.