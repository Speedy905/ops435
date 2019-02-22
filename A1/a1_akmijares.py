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

# Imports the sys module
import sys

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
def dbda(date, day):
    error = usage()
    try:
        num = int(day)
        tmpdate = date
        valid = valid_date(date)
        if valid == False:
            sys.exit()
        else:
            while num != 0:
                if num > 0:
                    tmpdate = tomorrow(tmpdate)
                    num = num - 1
                else:
                    tmpdate = yesterday(tmpdate)
                    num = num + 1
        error = usage()
        tar = tmpdate
        return tar
    except ValueError:
        return error

# tomorrow function
# Adds number of days after date
# If adding the day goes to the new month/year
# It adapts to the new month/year
def tomorrow(currentdate):
    # Declares the steparg variable global
    global steparg
    
    if len(currentdate) !=8:
        print ("Error: wrong date entered")
    else:
        currentyear = int(currentdate[0:4])
        currentmonth = int(currentdate[4:6])
        currentday = int(currentdate[6:])
        maximum_in_month = days_in_mon(currentyear)
        tmp_month1 = currentmonth
        tmp_day1 = currentday + 1
		# If the days go to a new month, it resets itself back to 
		# the start of the day, otherwise, nothing has been changed
        if tmp_day1 > maximum_in_month[currentmonth]:
			# Resets day back to 01 if it goes to a new month
            to_day1 = tmp_day1 % maximum_in_month[currentmonth] 
            tmp_month1 = tmp_month1 + 1
        else:  
            to_day1 = tmp_day1
            tmp_month1 = currentmonth + 0
            
        if tmp_month1 > 12:
            to_month1 = 1
            currentyear = currentyear + 1
        else:
            to_month1 = tmp_month1 + 0

    # Stores the stripped variables into a string
        next_date = str(currentyear) + \
        str(to_month1).zfill(2) + str(to_day1).zfill(2)

    # If the steparg variable is True when the program was ran,
    # It prints out all the days until the destination
    # If False, it just returns the result
        if steparg == True:
            print(next_date)
            return next_date
        else:
            return next_date


# yesterday function
# Subtracts the number of days before date
# If subtracting goes to an older month/year
# It adapts to the new month/year
def yesterday(current):
    # Declares the steparg variable global
    global steparg
    if len(current) != 8:
        print("Error: wrong date entered")
    else:
        currentyear = int(current[0:4])
        currentmonth = int(current[4:6])
        currentday = int(current[6:])
        currentday_tmp = currentday - 1
        month_max = days_in_mon(currentyear)

        if currentday_tmp == 0:
            # If the days go to a previous month, it resets itself 
            # Back to the max day of the month
            # Otherwise, nothing has changed
            tmp_month2 = currentmonth - 1
            if tmp_month2 == 0:
                tmp_month2 = 12
                to_day2 = month_max[tmp_month2]
                currentyear = currentyear - 1
            else:
                # If calculation reaches the previous month, 
                # Reset the day back to the maximim of the month
                to_day2 = month_max[tmp_month2] 
        else:
            to_day2 = currentday_tmp
            tmp_month2 = currentmonth + 0

        # If the calculation goes to a previous year,
        # The month gets reset back to the max month of the year
        # While also resetting the maximum day of the month
        if tmp_month2 == 0:
            to_month2 = 12
            currentyear = currentyear - 1
        else:
            to_month2 = tmp_month2 + 0

        # Stores the stripped variables into a string
        before_date = str(currentyear) + \
            str(to_month2).zfill(2) + str(to_day2).zfill(2)

    # If the steparg variable is True when the program was ran,
    # It prints out all the days until the destination
    # If False, it just returns the result
    if steparg == True:
        print(before_date)
        return before_date
    else:
        return before_date

# days_in_mon function
# While it also checks if it is a leap year
# It also stores the max day in a tuple
def days_in_mon(tmp_year):
    leapyear = tmp_year
    if leapyear % 4 == 0:
        febmax = 29
    elif leapyear % 100 == 0:
        febmax = 28
    elif leapyear % 400 == 0:
        febmax = 29
    else:
        febmax = 28

    leap_year(leapyear)
    month_max = {1: 31, 2: febmax, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                 9: 30, 10: 31, 11: 30, 12: 31}

    return month_max

# leap_year function
# Check if year is leapyear
# If it is, returns as True
# If not, returned as False
def leap_year(leap):
    l_year = leap
    if l_year % 4 == 0:
        return True
    elif l_year % 100 == 0:
        return False
    elif l_year % 400 == 0:
        return True
    else:
        return False

# validdate function
# Strips the variable
# Then runs through
# Statements to see if valid
# If valid, returns as True
# If not, calls one of the functions to 
# Print out the error
# While elso returning a False Statement
def valid_date(date):
    y = int(date[0:4])
    m = int(date[4:6])
    d = int(date[6:])
    tmp_d = d
    tmp_m = m
    days_in_month = days_in_mon(y)
    if tmp_m > 12 or tmp_m < 1:
        print(showmonth())
        return False
    else:
        if tmp_d > days_in_month[m]:
            print(showday())
            return False
        else:
            return True

# showmonth function
# If the month was entered wrong, it returns
# This statement
def showmonth():
    return "Error: wrong month entered"

# showday function
# If the day was entered wrong, it returns
# This statement
def showday():
    return "Error: wrong day entered"


# First part of the code that runs.
# It goes through if/elif/else statements to see
# If the program was executed properly
# If 2 arg were given (excluding the python file), 
# It stores it into a variable, which calls the dbda function
# If 3 arg were given (excluding the python file),
# It also checks if the first argument was executed properly
# If it is, it calls the dbda function
# If the program was not executed properly, it calls the usage 
# Function
if __name__ == "__main__":
    if len(sys.argv) == 3:
        d = sys.argv[1]
        n = sys.argv[2]
        steparg = False
        print(dbda(d, n))
    elif len(sys.argv) == 4:
        s = sys.argv[1]
        d = sys.argv[2]
        n = sys.argv[3]
        if s == "--step":
            steparg = True
            dbda(d, n)
        else:
            print(usage())
    else:
        print((usage()))
