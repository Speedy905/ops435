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
    return """
    Ways to use this program:
    a) YYYYMMDD [Positve or negative number, cannot be 0]
    b) YYYYMMDD --step [Positve or negative number, cannot be 0]
    """


try:
    date = sys.argv[1]
    number = sys.argv[2]
except:
    print (showusage())
