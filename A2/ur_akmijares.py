#!/usr/bin/env python3

# OPS435 Assignment 2 - Winter 2019
# Program: ur_akmijares.py
# Author: "Antonio Karlo Mijares"
# The python code in this file ur_akmijares.py is original work written by
# Antonio Karlo Mijares. No code in this file is copied from any other source
# including any person, textbook, or on-line resource except those provided
# by the course instructor. I have not shared this python file with anyone
# or anything except for submission for grading.
# I understand that the Academic Honesty Policy will be enforced and violators
# will be reported and appropriate action will be taken.

'''
   authorship declaration

   __author__ Antonio Karlo Mijares
   __date__ March 2019
   __version__ 1.0

   Calculate user usage for the day, week or month
'''

# Imports the needed modules
import sys
import argparse
import time


def getlist(filelist):
    '''If the user decides to display
    the info, it will search through
    the file and filter out the 
    appropriate variable'''
    file = open(filelist, 'r')
    fileRead = file.readlines()
    fileRead = fileRead[1::]
    NameList = []
    n = 0
    b = 0
    u = None

    if args.list == 'user':
        b = 0
        u = 'User'
    elif args.list == 'host':
        b = 2
        u = 'Host'

    for eachRecond in fileRead:
        temp = fileRead[n].split()
        NameList.append(temp[b])
        n = n + 1
    NameList = set(NameList)
    NameList = list(NameList)
    NameList.sort()

    login = u + ' ' + 'list for' + ' ' + filelist
    login += '\n'
    for length in range (1, len(login)):
        login += "="
    login += '\n'
    for eachName in NameList:
        login += eachName
        login += '\n'

    return login


def read_login_rec(subj, filelist):
    '''get records from given filelist
    open and read each file from the filelist
    filter out the unwanted records
    add filtered record to list (login_recs)'''
    login_rec = []
    # Opens the file, finds the line that have
    # The needed subject, and adds them to a list
    try:
        with open(filelist, 'r') as searching:
            for line in searching:
                line = line.split()
                if subj in line:
                    login_rec.append(line)

        
        # Returns the list
        return login_rec

    # Error exception when file is not found
    except FileNotFoundError:
        print("File not found")
        sys.exit()

def cal_daily_usage(subject, login_recs):
    '''generate daily usage report for the given
    subject (user or remote host)'''

    # Adds the string to the top of the "table"
    # With the border (being =) pritned by the length
    # of the title
    msg = ""
    msg += "Daily usage report for " + str(subject)
    msg += "\n"
    for length in range(1, len(msg)):
        msg += "="
    msg += "\n"
    msg += "Date"
    for lenth in range(4,14):
        msg += " "
    msg += "Usage in seconds"
    msg += "\n"

    # Creates empty lists and variables
    counter = 0
    daily_usage = 0
    diffdict = []
    tmp = []

    # Runs through a for loop, where it goes from
    # The beginning of the 2d array to the end, 
    # Starting with the inner array, selects the dates
    # Puts them into a string, then the time module
    # Puts them into tuples (being seconds), which
    # Then calculates the difference between the two dates
    # Which the data is then "displayed" for the user
    # Then repeats until there are no more dates that need
    # To be calculated 
    for item in range(0, len(login_recs)):
        #before = 0
        datelist = login_recs[counter]
        
        datetmp1 = datelist[3:8]
        datetmp2 = datelist[9:14]
        
        date1 = ' '.join(datetmp1)
        date2 = ' '.join(datetmp2)
        
        sec1 = time.mktime(time.strptime(date1, "%a %b %d %H:%M:%S %Y"))
        sec2 = time.mktime(time.strptime(date2, "%a %b %d %H:%M:%S %Y"))

        diff = sec2 - sec1

        diffdict.append(int(diff))

        days = sum(diffdict)

        daily_usage += diff 

        counter += 1 

        # Converts the tuple into a readable format
        datemsg = time.strftime("%Y %m %d", time.localtime(sec1))
        daily_usage = int(daily_usage)

        # Checks if the date already exists,
        # Which replaces the seconds into 
        # Another updated and calculated one
        if datemsg in msg:
            if t in msg:
                msg = msg.replace(t, str(days))
                #tmp = []
                #diffdict = []
                #pass
        else:
            msg += str(datemsg)
            for length in range (10,18):
                msg += " "
            msg += str(daily_usage)
            msg += "\n"

            tmp.append(str(int(diff)))
            t = ''.join(tmp)

            diffdict = []
            tmp = []
            days = 0

    # Displays the total amount of secs
    msg += "Total"
    for length in range (5,18):
        msg += " "
    msg += str(daily_usage)
    return msg


def cal_weekly_usage(subject, login_recs):
    '''generate weekly usage report for the given
    subject (user or remote host)'''

    # Adds the string to the top of the "table"
    # With the border (being =) pritned by the length
    # of the title
    msg = ""
    msg += "Weekly usage report for " + str(subject)
    msg += "\n"
    for length in range(1, len(msg)):
        msg += "="
    msg += "\n"
    msg += "Week #"
    for length in range(6,14):
        msg += " "
    msg += "Usage in seconds"
    msg += "\n"

    counter = 0
    weekly_usage = 0
    diffdict = []
    tmp = []

    # Runs through a for loop, where it goes from
    # The beginning of the 2d array to the end, 
    # Starting with the inner array, selects the dates
    # Puts them into a string, then the time module
    # Puts them into tuples (being seconds), which
    # Then calculates the difference between the two dates
    # Which the data is then "displayed" for the user
    # Then repeats until there are no more dates that need
    # To be calculated 
    for item in range(0, len(login_recs)):
        datelist = login_recs[counter]
        
        datetmp1 = datelist[3:8]
        datetmp2 = datelist[9:14]
        
        date1 = ' '.join(datetmp1)
        date2 = ' '.join(datetmp2)

        sec1 = time.mktime(time.strptime(date1, "%a %b %d %H:%M:%S %Y"))
        sec2 = time.mktime(time.strptime(date2, "%a %b %d %H:%M:%S %Y"))

        diff = sec2 - sec1

        diffdict.append(int(diff))

        days = sum(diffdict)

        weekly_usage += diff

        counter += 1

        datemsg = time.strftime("%Y %W", time.localtime(sec1))
        weekly_usage = int(weekly_usage)

        # Checks if the date already exists,
        # Which replaces the seconds into 
        # Another updated and calculated one
        if datemsg in msg:
            if t in msg:
                msg = msg.replace(t, str(days))
                tmp = []
                diffdict = []
        else:
            msg += str(datemsg)
            for length in range (7,19):
                msg += " "
            msg += str(weekly_usage)
            msg += "\n" 

            tmp.append(str(int(diff)))
            t = ''.join(tmp)
    
    msg += "Total"
    for length in range (5,19):
        msg += " "
    msg += str(weekly_usage)
    return msg


def cal_monthly_usage(subject, login_recs):
    '''generate monthly usage report fro the given
    subject (user or remote host)'''

    # Adds the string to the top of the "table"
    # With the border (being =) pritned by the length
    # of the title
    msg = ""
    msg += "Monthly usage report for " + str(subject)
    msg += "\n"
    for length in range (1,len(msg)):
        msg += "="
    msg += "\n"
    msg += "Month"
    for length in range (5,14):
        msg += " "
    msg += "Usage in seconds"
    msg += "\n"

    counter = 0
    monthly_usage = 0
    diffdict = []
    tmp = []

    # Runs through a for loop, where it goes from
    # The beginning of the 2d array to the end, 
    # Starting with the inner array, selects the dates
    # Puts them into a string, then the time module
    # Puts them into tuples (being seconds), which
    # Then calculates the difference between the two dates
    # Which the data is then "displayed" for the user
    # Then repeats until there are no more dates that need
    # To be calculated 
    for item in range(0, len(login_recs)):
        datelist = login_recs[counter]
        
        datetmp1 = datelist[3:8]
        datetmp2 = datelist[9:14]
        
        date1 = ' '.join(datetmp1)
        date2 = ' '.join(datetmp2)

        sec1 = time.mktime(time.strptime(date1, "%a %b %d %H:%M:%S %Y"))
        sec2 = time.mktime(time.strptime(date2, "%a %b %d %H:%M:%S %Y"))

        diff = sec2 - sec1


        diffdict.append(int(diff))

        days = sum(diffdict)

        monthly_usage += diff

        counter += 1

        datemsg = time.strftime("%Y %m", time.localtime(sec1))
        monthly_usage = int(monthly_usage)

        # Checks if the date already exists,
        # Which replaces the seconds into 
        # Another updated and calculated one
        if datemsg in msg:
            if t in msg:
                msg = msg.replace(t, str(days))
                tmp = []
                diffdict = []
        else:
            msg += str(datemsg)
            for length in range (7,19):
                msg += " "
            msg += str(monthly_usage)
            msg += "\n" 

            tmp.append(str(int(diff)))
            t = ''.join(tmp)
    
    msg += "Total"
    for length in range (5,19):
        msg += " "
    msg += str(monthly_usage)
    return msg


# Checks for arguments
if __name__ == "__main__":

    # Arrgances the arguments (positional and optional)
    parser = argparse.ArgumentParser(
        description="Usage Report based on the last command",
        epilog='Copyright 2019 - Antonio Karlo Mijares')
    parser.add_argument('F', help='list of files to be processed')
    parser.add_argument('-l', '--list', metavar='{user,host}',
                        type=str,
                        help='generate user name or remote host IP from the given files')
    parser.add_argument('-r', '--rhost',
                        type=str,
                        help='generate user name or remote host IP from the given files')
    parser.add_argument('-t', '--type',
                        metavar='{daily,weekly,monthly}',
                        type=str, help='type of report: daily,weekly, and monthly')
    parser.add_argument('-u', '--user',
                        type=str, help='usage report for the given username')
    parser.add_argument('-v', '--verbose',
                        help='tune on output verbosity',
                        action='store_true')
    args = parser.parse_args()

    # If verbose is selected, it is prints out the processes
    if args.verbose:
        print("Files to be processed: " + str(args.F))
        print("Type of args for files <class 'list'>")

    # If List is selected, it displays the table of the 
    # Existing users or hosts
    if args.list:
        print(getlist(args.F))

    # If user is selected
    # It then goes through another condition
    # Where it checks if daily, weekly, or monthly
    # Needs to be calc, where it then calls the appropriate
    # Function
    if args.user:
        if args.type == 'daily':
            # If verbose is selected, it prints out
            # The rest of the processes
            if args.verbose:
                print("Usage report for user: " + str(args.user))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            filetouse = read_login_rec(args.user, args.F)
            print(cal_daily_usage(args.user, filetouse))
        elif args.type == 'weekly':
            # If verbose is selected, it prints out
            # The rest of the processes
            if args.verbose:
                print("Usage report for user: " + str(args.user))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            filetouse = read_login_rec(args.user, args.F)
            print(cal_weekly_usage(args.user, filetouse))
        elif args.type == 'monthly':
            # If verbose is selected, it prints out
            # The rest of the processes
            if args.verbose:
                print("Usage report for user: " + str(args.user))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            filetouse = read_login_rec(args.user, args.F)
            print(cal_monthly_usage(args.user, filetouse))

    # If user is selected
    # It then goes through another condition
    # Where it checks if daily, weekly, or monthly
    # Needs to be calc, where it then calls the appropriate
    # Function
    if args.rhost:
        if args.type == 'daily':
            # If verbose is selected, it prints out
            # The rest of the processes
            if args.verbose:
                print("Usage report for remote host: " + str(args.rhost))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            filetouse = read_login_rec(args.rhost, args.F)
            print(cal_daily_usage(args.rhost, filetouse))
        elif args.type == 'weekly':
            # If verbose is selected, it prints out
            # The rest of the processes
            if args.verbose:
                print("Usage report for remote host: " + str(args.rhost))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            filetouse = read_login_rec(args.rhost, args.F)
            print(cal_weekly_usage(args.rhost, filetouse))
        elif args.type == 'monthly':
            # If verbose is selected, it prints out
            # The rest of the processes
            if args.verbose:
                print("Usage report for rhost: " + str(args.rhost))
                print("Usage report type: " + str(args.type))
                print("Processing usage report for the following:")
                print("reading login/logout record files " + str(args.F))
            filetouse = read_login_rec(args.rhost, args.F)
            print(cal_monthly_usage(args.rhost, filetouse))
