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

# Imports the sys and os modules
import sys
import os

# usage function
# Shows the user how they should use the program properly
def usage():
    return "Usage: akmijares.py [--step] YYYYMMDD +/-n"

# dbda function
# It goes through an exception checking
# whether or not its ran properly or not
# If the arguments were not given properly
# it calls the usage function
# Otherwise it goes to a loop where it calls
# Either the tomorrow, or the yesterday function
def dbda(date, days):
    error= usage()
    try:
        x = int(days)
        tmp_date = date
        vdate = valid_date(date)
        if vdate == False:
            sys.exit()
        else:
            while x != 0:   
                if x > 0:        
                    tmp_date = tomorrow(tmp_date)
                    x = x - 1
                else:
                    tmp_date = yesterday(tmp_date)
                    x = x + 1
        error= usage()
        target_day = tmp_date 
        return target_day
    except ValueError:
        return error

# tomorrow function
# Adds number of days after date
# If adding the day goes to the new month/year
# It adapts to the new month/year
def tomorrow(today):
    if len(today) != 8:
       print(usage())
    else:
        year = int(today[0:4])
        month = int(today[4:6])
        day = int(today[6:])
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
            year = year +  1
        else:
            to_month = tmp_month + 0
        next_date = str(year)+str(to_month).zfill(2)+str(to_day).zfill(2)
     
        return next_date    

# yesterday function
# Subtracts the number of days before date
# If subtracting goes to an older month/year
# It adapts to the new month/year
def yesterday(today):
    if len(today) != 8:
       print(usage())
    else:
        year = int(today[0:4])
        month = int(today[4:6])
        day = int(today[6:])
        tmp_day = day - 1 
    
        month_max = days_in_mon(year)
       
        tmp_month = month
        tmp_day = day - 1 
        if tmp_day < month_max[month]:
            to_day = tmp_day % month_max[month] 
            tmp_month = tmp_month - 1
            
        else:
           to_day = tmp_day
           tmp_month = month - 0
        
        if tmp_month < 1:
            to_month = 1
            year = year -  1
        else:
            to_month = tmp_month - 0

        before_date = str(year)+str(to_month).zfill(2)+str(to_day).zfill(2)

        return before_date

# days_in_mon function
# While it also checks if it is a leap year
# It also stores the max day in a tuple
def days_in_mon(tmp_year):
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
    mon_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 
    9:30, 10:31, 11:30, 12:31}
    return mon_max
    
# leap_year function
# Check if year is leapyear
# If it is, returns as True
# If not, returned as False
def leap_year(lpyear):
    
    leap_year = lpyear
    if leap_year % 4 ==  0:
        return True
    elif leap_year % 100 == 0:
        return False
    elif leap_year % 400 == 0:
        return True
    else:
        return False

# validdate function
# Strips the variable
# Then runs through 
# Statements to see if valid
# If valid, returns as True
# If not, prints an error.
def valid_date(today):
    
    year = int(today[0:4])
    month = int(today[4:6])
    day = int(today[6:])
    tmp_day = day
    tmp_month = month
    days_month = days_in_mon(year)
    if tmp_month > 12 or tmp_month < 1:
        print(showmonth())
        return False
    else:
        if tmp_day > days_month[month]:
            print(showday())
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
    if len(sys.argv) == 3:
        d = sys.argv[1]
        n = sys.argv[2]
        print(dbda(d, n))
    else:
        print((usage()))