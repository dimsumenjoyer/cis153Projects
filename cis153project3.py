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

def find_requester_resource():
    file = open("access_log.txt", "r")
    read_file = file.readlines()
    requester_time_resource = "^(\S+) - - \[.+\] \"[A-Z]+ (\S+) "
    locate_stuff = re.compile(requester_time_resource)
    requester = ""
    resource = ""
    requesters_resources = {}
    for line in read_file:
        stuff = locate_stuff.findall(line)
        if len(stuff) > 0:
            [(requester, resource)] = stuff
            print(requester)
            print(resource)
    file.close()
    return

find_requester_resource()

def resources():
    resource = r'\"GET\s(.*?)\sHTTP\/1\.1\"\s(\d+)\s(\d+)'
    return

def requester_to_resources():
    #example = {"requester", "resource", "number_of_accessed"}
    return