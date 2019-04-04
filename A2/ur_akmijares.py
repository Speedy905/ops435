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

import sys
import os
import argparse
import time


#date1 = None
#date2 = None

def getlist(filelist):
    file = open(filelist, 'r')
    fileRead = file.readlines()
    fileRead = fileRead[1::]
    NameList = []
    n = 0
    b = 0
    u = None

    if args.list == 'user':
        b = 0
        u = 'user'
    elif args.list == 'host':
        b = 2
        u = 'host'

    for eachRecond in fileRead:
        temp = fileRead[n].split()
        NameList.append(temp[b])
        n = n + 1
    NameList = set(NameList)
    NameList = list(NameList)
    NameList.sort()

    login = u + ' ' + 'list for' + ' ' + filelist + '\n' '=============================' '\n'
    for eachName in NameList:
        login += eachName
        login += '\n'

    return login


def read_login_rec(subj, filelist):
    ''' docstring for this function
    get records from given filelist
    open and read each file from the filelist
    filter out the unwanted records
    add filtered record to list (login_recs)'''
    login_rec = []
    try:
        with open(filelist, 'r') as searching:
            for line in searching:
                line = line.split()
                if subj in line:
                    login_rec.append(line)

        
        #print(login_rec)
        return login_rec

    except FileNotFoundError:
        print("File not found")
        sys.exit()

def cal_daily_usage(subject, login_recs):
    ''' docstring for this function
    generate daily usage report for the given
    subject (user or remote host)'''

    #global date1
    #global date2

    date1 = "Lol"
    date2 = "Lol"

    msg = ""
    msg += "Daily usage report for " + str(subject)
    msg += "\n"
    msg += "======================================="
    msg += "\n"
    msg += "Date                   Usage in seconds"
    msg += "\n"

    counter = 0
    daily_usage = 0
    for item in range(0, len(login_recs)):
        tempstring = ' '.join(login_recs[counter])

        lengthlist = len(tempstring)

        if lengthlist == 84:
            date1 = tempstring[25:49]
            date2 = tempstring[52:76]
        elif lengthlist == 85:
            date1 = tempstring[26:50]
            date2 = tempstring[53:77]
        elif lengthlist == 86:
            date1 = tempstring[27:51]
            date2 = tempstring[54:78]

        sec1 = time.mktime(time.strptime(date1, "%a %b %d %H:%M:%S %Y"))
        sec2 = time.mktime(time.strptime(date2, "%a %b %d %H:%M:%S %Y"))

        diff = sec2 - sec1

        daily_usage += diff

        counter += 1

    datemsg = time.strftime("%Y %m %d", time.localtime(sec2))
    daily_usage = int(daily_usage)
    msg += str(datemsg) + "                 " + str(daily_usage)
    msg += "\n" 
    
    msg += "Total" + "                      " + str(daily_usage)
    return msg


def cal_weekly_usage(subject, login_recs):
    ''' docstring for this function
    generate weekly usage report for the given
    subject (user or remote host)'''

    msg = ""
    msg += "Weekly usage report for " + str(subject)
    msg += "\n"
    msg += "======================================="
    msg += "\n"
    msg += "Date                   Usage in seconds"
    msg += "\n"

    counter = 0
    weekly_usage = 0
    for item in range(0, len(login_recs)):
        tempstring = ' '.join(login_recs[counter])

        lengthlist = len(tempstring)

        if lengthlist == 84:
            date1 = tempstring[25:49]
            date2 = tempstring[52:76]
        elif lengthlist == 85:
            date1 = tempstring[26:50]
            date2 = tempstring[53:77]
        elif lengthlist == 86:
            date1 = tempstring[27:51]
            date2 = tempstring[54:78]

        sec1 = time.mktime(time.strptime(date1, "%a %b %d %H:%M:%S %Y"))
        sec2 = time.mktime(time.strptime(date2, "%a %b %d %H:%M:%S %Y"))

        diff = sec2 - sec1

        weekly_usage += diff

        counter += 1

    datemsg = time.strftime("%Y %m %d", time.localtime(sec1))
    weekly_usage = int(weekly_usage)
    msg += str(datemsg) + "                 " + str(weekly_usage)
    msg += "\n" 
    
    msg += "Total" + "                      " + str(weekly_usage)
    return msg


def cal_monthly_usage(subject, login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''


    msg = ""
    msg += "Monthly usage report for " + str(subject)
    msg += "\n"
    msg += "======================================="
    msg += "\n"
    msg += "Date                   Usage in seconds"
    msg += "\n"

    counter = 0
    monthly_usage = 0
    for item in range(0, len(login_recs)):
        tempstring = ' '.join(login_recs[counter])

        lengthlist = len(tempstring)

        if lengthlist == 84:
            date1 = tempstring[25:49]
            date2 = tempstring[52:76]
        elif lengthlist == 85:
            date1 = tempstring[26:50]
            date2 = tempstring[53:77]
        elif lengthlist == 86:
            date1 = tempstring[27:51]
            date2 = tempstring[54:78]

        sec1 = time.mktime(time.strptime(date1, "%a %b %d %H:%M:%S %Y"))
        sec2 = time.mktime(time.strptime(date2, "%a %b %d %H:%M:%S %Y"))

        diff = sec2 - sec1

        monthly_usage += diff

        counter += 1

    datemsg = time.strftime("%Y %m %d", time.localtime(sec1))
    monthly_usage = int(monthly_usage)
    msg += str(datemsg) + "                 " + str(monthly_usage)
    msg += "\n" 
    
    msg += "Total" + "                      " + str(monthly_usage)
    return msg


# Checks for arguments
if __name__ == "__main__":
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
                        metavar='', help='tune on output verbosity')
    args = parser.parse_args()

    if args.list:
        print(getlist(args.F))

    if args.user:
        if args.type == 'daily':
            filetouse = read_login_rec(args.user, args.F)
            print(cal_daily_usage(args.user, filetouse))
        elif args.type == 'weekly':
            filetouse = read_login_rec(args.user, args.F)
            print(cal_weekly_usage(args.user, filetouse))
        elif args.type == 'monthly':
            filetouse = read_login_rec(args.user, args.F)
            print(cal_monthly_usage(args.user, filetouse))

    if args.rhost:
        if args.type == 'daily':
            filetouse = read_login_rec(args.rhost, args.F)
            print(cal_daily_usage(args.rhost, filetouse))
        elif args.type == 'weekly':
            filetouse = read_login_rec(args.rhost, args.F)
            print(cal_weekly_usage(args.rhost, filetouse))
        elif args.type == 'monthly':
            filetouse = read_login_rec(args.rhost, args.F)
            print(cal_monthly_usage(args.rhost, filetouse))

    if args.verbose:
        print('test2')