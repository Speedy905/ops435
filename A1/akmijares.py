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

# usage function
# Shows the user how they should use the program properly
def usage():
    return "Usage: akmijares.py [--step] YYYYMMDD +/-n"

# tomorrow function
# Adds number of days after date
# If adding the day goes to the new month/year
# It Changes so that, it'll also change to the next
# month or year
def tomorrow(datevar, numtoadd, leapcheck):
    if leapcheck == True:
        feb = 29
    elif leapcheck == False:
        feb = 28
    month_maximum = {1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    datevarstring = str(datevar)
    currentyear = int(datevarstring[0:4])
    currentmonth = int(datevarstring[4:6])
    currentday = int(datevarstring[6:])
    #stepvar = int(datevar) + 1
    afterday = currentday + numtoadd
    
    # Checks how many months to add
    if afterday > month_maximum[currentmonth]:
        after_day = afterday % month_maximum[currentmonth]
        aftermonth = 0
        if numtoadd >=30 and numtoadd < 60:
            aftermonth = currentmonth + 1
        elif numtoadd >=60 and numtoadd < 90:
            aftermonth = currentmonth + 2
        elif numtoadd >=90 and numtoadd < 120:
            aftermonth = currentmonth + 3
    else:
        after_day = afterday
        aftermonth = currentmonth + 0
        
    if aftermonth > 12:
        resetmonth = 1
        currentyear = currentyear + 1
    else:
        resetmonth = aftermonth + 0
        
    afterdate = str(currentyear)+str(resetmonth).zfill(2)+str(after_day).zfill(2)
    
    #if stepcheck == True:
     #   for x in 1:
      #      print (stepvar)
       #     if afterday == afterdate:
        #        break
    #else:
    print (afterdate)

# yesterday function
# Subtracts number of days before date
# Also converts negative integer to positive
# before subtracting
def yesterday(datevar2, numtosub, leapcheck2):
    if leapcheck2 == True:
        feb = 29
    elif leapcheck2 == False:
        feb = 28
    month_maximum2 = {1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    datevarstring2 = str(datevar2)
    currentyear2 = int(datevarstring2[0:4])
    currentmonth2 = int(datevarstring2[4:6])
    currentday2 = int(datevarstring2[6:])
    positive= abs(numtosub)
    beforeday = datevar2 - positive
    
    if beforeday > month_maximum2[currentmonth2]:
        before_day = beforeday % month_maximum2[currentmonth2]
        beforemonth = currentmonth2 - 1
    else:
        before_day = beforeday
        beforemonth = currentmonth2 + 1
        
    if beforemonth < 1:
        resetmonth2 = 1
        currentyear2 = currentyear2 - 1
    else:
        resetmonth2 = beforemonth + 0
        
    beforedate = str(currentyear2)+str(resetmonth2).zfill(2)+str(before_day).zfill(2)
    print (beforedate)

# checknums function
# Checks if the arguments given are proper
# If they are, it calls the functions
def checknums(datearg, numarg):
    if len(str(datearg)) == 8:
        valid_date(int(datearg), numarg)

    else:
        print(usage())

# showmonth function
# If error has occured, it prints this
def showmonth():
    return "Error: wrong month entered"

# showday function
# If error has occured, it prints this
def showday():
    return "Error: wrong day entered"

# validdate function
# Converts date to string, so it can be
# stripped, then it checks to see
# if numbers are in range. 
# If in range, considered valid date
# If not, prints out error message. 
def valid_date(datecheck, numint):
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4,6,9,11]
    
    datestring= str(datecheck)
    year = datestring[0:4]
    month = datestring[4:6]
    day = datestring[6:]
    
    
    yearint = int(year)
    monthint = int(month)
    dayint = int(day)
    
    leap = yearint % 4
    leap2 = yearint % 100
    leap3 = yearint % 400
    
    # Big if statements
    # Checks the date
    # Regardless if leap year or not
    if leap == 0:
        if leap2 == 0:
            if leap3 == 0:
                leap_year = True
                if monthint > 0 and monthint <=12:
                    if monthint in month31:
                        if dayint >=1 and dayint <=31:
                            if numint > 0:
                                tomorrow(datecheck, numint, leap_year)
                            elif numint < 0:
                                yesterday(datecheck, numint, leap_year)
                        else:
                            print (showday())
                    elif monthint in month30:
                        if dayint >=1 and dayint <=30:
                            if numint > 0:
                                tomorrow(datecheck, numint, leap_year)
                            elif numint < 0:
                                yesterday(datecheck, numint, leap_year)
                        else:
                            print (showday())
                    elif monthint == 2:
                        if dayint >=1 and dayint <=29:
                            leap_year = True
                            if numint > 0:
                                tomorrow(datecheck, numint, leap_year)
                            elif numint < 0:
                                yesterday(datecheck, numint, leap_year)
                        else:
                            print (showday())
                else:
                    print (showmonth())
            else:
                leap_year = False
                if monthint > 0 and monthint <=12:
                    if monthint in month31:
                        if dayint >=1 and dayint <=31:
                            if numint > 0:
                                tomorrow(datecheck, numint, leap_year)
                            elif numint < 0:
                                yesterday(datecheck, numint, leap_year)
                        else:
                            print (showday())
                    elif monthint in month30:
                        if dayint >=1 and dayint <=30:
                            if numint > 0:
                                tomorrow(datecheck, numint, leap_year)
                            elif numint < 0:
                                yesterday(datecheck, numint, leap_year)
                        else:
                            print (showday())
                    elif monthint == 2:
                        if dayint >=1 and dayint <=28:
                            if numint > 0:
                                tomorrow(datecheck, numint, leap_year)
                            elif numint < 0:
                                yesterday(datecheck, numint, leap_year)
                        else:
                            print (showday())
                    else:
                        print (showmonth())
        else:
            leap_year = True
            if monthint > 0 and monthint <=12:
                if monthint in month31:
                    if dayint >=1 and dayint <=31:
                        if numint > 0:
                            tomorrow(datecheck, numint, leap_year)
                        elif numint < 0:
                            yesterday(datecheck, numint, leap_year)
                    else:
                        print (showday())
                elif monthint in month30:
                    if dayint >=1 and dayint <=30:
                        if numint > 0:
                            tomorrow(datecheck, numint, leap_year)
                        elif numint < 0:
                            yesterday(datecheck, numint, leap_year)
                    else:
                        print (showday())
                elif monthint == 2:
                    if dayint >=1 and dayint <=29:
                        if numint > 0:
                            tomorrow(datecheck, numint, leap_year)
                        elif numint < 0:
                            yesterday(datecheck, numint, leap_year)
                    else:
                        print (showday())
            else:
                print (showmonth())
    else:
        leap_year = False
        if monthint > 0 and monthint <=12:
            if monthint in month31:
                if dayint >=1 and dayint <=31:
                    if numint > 0:
                        tomorrow(datecheck, numint, leap_year)
                    elif numint < 0:
                        yesterday(datecheck, numint, leap_year)
                else:
                    print (showday())
            elif monthint in month30:
                if dayint >=1 and dayint <=30:
                    if numint > 0:
                        tomorrow(datecheck, numint, leap_year)
                    elif numint < 0:
                        yesterday(datecheck, numint, leap_year)
                else:
                    print (showday())
            elif monthint == 2:
                if dayint >=1 and dayint <=28:
                    if numint > 0:
                        tomorrow(datecheck, numint, leap_year)
                    elif numint < 0:
                        yesterday(datecheck, numint, leap_year)
                else:
                    print (showday())
        else:
            print (showmonth())

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
    global stepcheck
    if len(sys.argv) == 3:
        try:
            date = int(sys.argv[1])
            number = int(sys.argv[2])
            checknums(date, number)
        except ValueError: 
            print(usage())
    elif len(sys.argv) == 4:
        try:
            steparg = str(sys.argv[1])
            date = int(sys.argv[2])
            number = int(sys.argv[3])
            if steparg == "--step":
                stepcheck = True
                checknums(date, number)
            else:
                print(usage())
        except ValueError:
            print (usage())
    else:
        print (usage())

# First part of the code that runs. 
# Calls the dbda function
if __name__ == "__main__":
    stepcheck = False
    dbda()
