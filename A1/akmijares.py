#!/usr/bin/env python3

# OPS435 Assignment 1 - Winter 2019
# Program: akmijares.py (replace student_id with your Seneca User name)
# Author: "Antonio Karlo Mijares"
# The python code in this file (akmijares.py) is original work written 
# by
# Antonio Karlo Mijares. No code in this file is copied from any other 
# source 
# except those provided by the course instructor, including any person, 
# textbook, or on-line resource. I have not shared this python script 
# with anyone or anything except for submission for grading.  
# I understand that the Academic Honesty Policy will be enforced and 
# violators will be reported and appropriate action will be taken.

#Imports the sys and os modules
import sys, os

# usage function
# Shows the user how they should use the program properly
def usage():
    return "Usage: akmijares.py [--step] YYYYMMDD +/-n"

# dbda function
# It goes through an exception checking
# whether or not its ran properly or not
# If the arguments were not given properly
# it calls the usage function
# Otherwise it goes through a bunch of 
# if/elif/else statements
# to see if the arguments are right
# If it is, it calls the function
# If not, it calls the usage function
def dbda():
    if len(sys.argv) == 3:
        try:
            date = sys.argv[1]
            number = sys.argv[2]
            tomorrow(date, number)
        except ValueError: 
            print(usage())
    elif len(sys.argv) == 4:
        try:
            steparg = str(sys.argv[1])
            date = int(sys.argv[2])
            number = int(sys.argv[3])
            if steparg == "--step":
                stepcheck = True
                #checknums(date, number)
            else:
                print(usage())
        except ValueError:
            print (usage())
    else:
        print (usage())
        
def leap_year(year):
	leap = int(year)
	if leap % 4 == 0:
		return True 
	elif leap % 100 == 0:
		return False
	elif leap % 400 == 0:
		return True
	else:
		return False
		
# tomorrow function
# Adds number of days after date
# If adding the day goes to the new month/year
# It Changes so that, it'll also change to the next
# month or year
def tomorrow(datevar): 
	if len(datevar) != 8:
		print(usage())
	else:
		year = int(datevar[0:4])
		month = int(datevar[4:6])
		day = int(datevar[6:])
		mont_max = days_in_mon(year)
		tmp_month = month
		tmp_day = day + 1
		
		if tmp_day > mont_max[month]:
			to_day = tmp_day % mont_max[month] 
			tmp_month = tmp_month + 1
		else:
			to_day = tmp_day
			tmp_month = month + 0
		
		if tmp_month > 12:
			to_month = 1
			year = year + 1
		else:
			to_month = tmp_month + 0
			
        afterdate = str(year)+str(to_month).zfill(2)+str(to_day).zfill(2)
        
        print(afterdate)
        
def days_in_mon(tempyear):
	lpyear = tmp_year
    if lpyear % 4 ==  0:
        feb_max = 29
    elif lpyear % 100 == 0:
        feb_max = 28
    elif lpyear % 400 == 0:
        feb_max = 29 
    else:
        feb_max = 28 
    leap_year(lpyear)
    mon_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 
	7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	
    return mon_max
    
# validdate function
# Converts date to string, so it can be
# stripped, then it checks to see
# if numbers are in range. 
# If in range, considered valid date
# If not, prints out error message. 
def valid_date(datecheck):
	year = int(today[0:4])
    month = int(today[4:6])
    day = int(today[6:])
    tmp_day = day
    tmp_month = month
    days_month = days_in_mon(year)
    if tmp_day > days_month[month]:
        print(showday())
        return False
    elif tmp_month > days_month[month]:
        return False
    elif tmp_day > days_month[month]:
        return False
    else:
        return True
        
# showmonth function
# If error has occured, it prints this
def showmonth():
    return "Error: wrong month entered"
    
# showday function
# If error has occured, it prints this
def showday():
    return "Error: wrong day entered"
    
# First part of the code that runs. 
# Calls the dbda function
if __name__ == "__main__":
	stepcheck = False
	dbda()
