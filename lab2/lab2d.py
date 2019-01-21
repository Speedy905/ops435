#!/usr/bin/env python3

# Antonio Karlo Mijares

# Imports sys
import sys

#Check if file called has 3 arguments
#If it does, it prints out the info
if len(sys.argv) == 3:
	name = sys.argv[1]
	age = sys.argv[2]
	print ('Hi ' + name + ', you are ' + age + ' years old.')
	sys.exit()
	

#If file has no or too many arguments,
#It prints out this message
print ('Usage: ./lab2d.py name age')
sys.exit()
