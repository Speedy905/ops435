#!/usr/bin/env python3

#OPS435 Assignment 2 - Winter 2019
#Program: ur_akmijares.py
#Author: "Antonio Karlo Mijares"
#The python code in this file ur_akmijares.py is original work written by
#Antonio Karlo Mijares. No code in this file is copied from any other source 
#including any person, textbook, or on-line resource except those provided
#by the course instructor. I have not shared this python file with anyone
#or anything except for submission for grading.  
#I understand that the Academic Honesty Policy will be enforced and violators 
#will be reported and appropriate action will be taken.

'''
   authorship declaration

   __author__ Antonio Karlo Mijares
   __date__ March 2019
   __version__ 1.0
 
   text to describe the purpose of this script
'''

import sys
import os
import argparse
import time

def get_login_rec():
    ''' docstring for this fucntion
    get records from the last command
    filter out the unwanted records
    add filtered record to list (login_recs)'''
    login_recs = os.system("last -Fiw")
    return login_recs
 
def read_login_rec(filelist):
    ''' docstring for this function
    get records from given filelist
    open and read each file from the filelist
    filter out the unwanted records
    add filtered record to list (login_recs)''' 
    #return login_rec

def cal_daily_usage(subject,login_recs):
    ''' docstring for this function
    generate daily usage report for the given 
    subject (user or remote host)'''
    #return daily_usage

def cal_weekly_usage(subject,login_recs):
    ''' docstring for this function
    generate weekly usage report for the given 
    subject (user or remote host)'''
    #return weekly_usage

def cal_monthly_usage(subject,login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''
    #return monthly_usage


# Checks for arguments
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("F", help="list of files to be processed")
	args = parser.parse_args()
	print(args.F)

