'''
Victor Van
00319912
CIS153: Project 3
11/1/2023, Due: 11/22/2023
'''

#example1 = {"requester": "resource": number_of_accessed}
#example2 = {(requester, resource): number_of_accessed} 

import re

def log():
    file = open("access_log.txt", "r")
    print(file.read())   
    return file

#log()

def requester():
    file = open("access_log.txt", "r")
    read_file = file.readlines()
    find_requester = r'\b^([\w.-]+)\b'
    find_requesters = re.compile(find_requester)
    requesters_resources = {}
    #find_requesters = re.compile(find_requester)
    #matches = line.findall(find_requesters)
    for line in read_file:
        match_requesters = find_requesters.findall(line)
        print(match_requesters) # test. It works!
    if match_requesters not in requesters_resources:
        #test_requesters[match_requesters] = 1
    #else:
        #test_requesters[match_requesters] += 1
    file.close()
    return

requester()

def resources():
    resource = r'\"GET\s(.*?)\sHTTP\/1\.1\"\s(\d+)\s(\d+)'
    return

def requester_to_resources():
    #example = {"requester", "resource", "number_of_accessed"}
    return