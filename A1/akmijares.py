#!/usr/bin/env python3

# OPS435 Assignment 1 - Winter 2019
# Program: akmijares.py (replace student_id with your Seneca User name)
# Author: "Antonio Karlo Mijares"
# The python code in this file (akmijares.py) is original work written by
# Antonio Karlo Mijares. No code in this file is copied from any other source 
# except those provided by the course instructor, including any person, 
# textbook, or on-line resource. I have not shared this python script 
# with anyone or anything except for submission for grading.  
# I understand that the Academic Honesty Policy will be enforced and 
# violators will be reported and appropriate action will be taken.

#Imports the sys and os modules
import sys, os

# showusage function
# Shows the user how they should use the program properly
def showusage():
    return "Usage: akmijares.py [--step] YYYYMMDD +/-n"

# First part of the code that runs. 
# It goes through an exception checking
# whether or not its ran properly or not
# If the arguments were not given properly
# it calls the showusage function
# Otherwise it goes through a bunch of 
# if/elif/else statements
# to see if the arguments are right
# If it is, it calls the function
# If not, it calls the showusage function
try:
    if len(sys.argv) == 3:
        date = int(sys.argv[1])
        number = int(sys.argv[2])
    elif len(sys.argv) == 4:
        date = int(sys.argv[1])
        number = int(sys.argv[3])
        steparg = str(sys.argv[2])
        if steparg == "--step":
            print ('test')
        else:
            print(showusage())
except:
    print (showusage())
