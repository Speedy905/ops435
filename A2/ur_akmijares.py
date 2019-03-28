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


import sys
import os
import argparse
import time


# Checks for arguments
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("F", help="list of files to be processed")
	args = parser.parse_args()
	print(args.F)