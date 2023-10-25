Victor Van 00319912
CIS153: Project 2 
Professor Penta
10/25/2023, Due: 11/1/2023

As of writing this, I have not finished debugging my code yet:

My bugs are if you press 3 for display_review_log, it ends up with an infinite loop. 
If you press 1, it keeps on asking for your first and last name infinitely 
& it doesn't append the users.md or log_file.md files also,
if you press one for login, it asks you for your username, but it doesn't seem to be checking 
users.md for the username & just asks for my given name and surname infinitely.
Option 1 is only supposed to check the inputed_username to see if the username exists in
the users.md file and checks if the password matches.
Option 2 is only supposed for be creating an account (username & password).
If you press 3, it also asks for your given name and surname indefinitely.
There seems to be a lot of issues with infinite loops despite not using while loops,
which is confusing to me. The only thing that works properly, is exiting the menu.

__________________________________________________________________________________________________