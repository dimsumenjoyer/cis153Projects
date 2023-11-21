'''
Victor Van
00319912
CIS153: Project 3
11/1/2023, Due: 11/22/2023
'''

In this project, I struggled with coming up with a regular expression. Professor Penta helped me come up with the regular expression:
"^(\S+) - - \[.+\] \"[A-Z]+ (\S+) ".

I also had issues with avoiding using intermedate data structures before storing the data from the log file into dictionaries
which cause memory issues so I had to condense my log function into my parse_lines function.

I used a for loop to search for matches of the regular expression, and then multiple if statements to sort them accordingly to 
their dictionaries.

For the find_most_requested_resource(resources) and find_most_active_requester(requesters) functions, I checked the requesters 
and resources dictionaries for the most occurances of requesters and resources.

In find_requester_resource, I printed out all of my results:
-Requester with most requests: 64.242.88.10 - 452 requests.
-Top requester of most requested resource: mail.geovariances.fr - 10 requests.
-Most requested resource: /twiki/pub/TWiki/TWikiLogos/twikiRobot46x50.gif - 64 total requests.

All log files in this format should be able to use this program to search this information.