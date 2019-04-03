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


def read_login_rec(filelist):
    ''' docstring for this function
    get records from given filelist
    open and read each file from the filelist
    filter out the unwanted records
    add filtered record to list (login_recs)'''
    # os1 = "pts"
    try:
        fileopen = open(filelist, 'r')
        login_rec = fileopen.readline()
        return login_rec
    except FileNotFoundError:
        print("File not found")
        sys.exit()


def cal_daily_usage(subject, login_recs):
    ''' docstring for this function
    generate daily usage report for the given
    subject (user or remote host)'''

    if subject in login_recs:
        line = login_recs
    else:
        print ('Not in file.')


# return daily_usage


def cal_weekly_usage(subject, login_recs):
    ''' docstring for this function
    generate weekly usage report for the given
    subject (user or remote host)'''


# return weekly_usage


def cal_monthly_usage(subject, login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''


# return monthly_usage


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
        if args.list == 'user':
            print('1')
        elif args.list == 'host':
            print('2')

    elif args.user:
       if args.type:
           if args.type == 'daily':
               filetouse = read_login_rec(args.F)
               cal_daily_usage(args.user, filetouse)
           elif args.type == 'weekly':
               filetouse = read_login_rec(args.F)
               cal_weekly_usage(args.user, filetouse)
           elif args.type == 'monthly':
               filetouse = read_login_rec(args.F)
               cal_monthly_usage(args.user, filetouse)
    elif args.rhost:
       if args.type:
           if args.type == 'daily':
               filetouse = read_login_rec(args.F)
               cal_daily_usage(args.rhost, filetouse)
           elif args.type == 'weekly':
               filetouse = read_login_rec(args.F)
               cal_weekly_usage(args.rhost, filetouse)
           elif args.type == 'monthly':
               filetouse = read_login_rec(args.F)
               cal_monthly_usage(args.rhost, filetouse)
