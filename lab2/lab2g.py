#!/usr/bin/env python3

# Antonio Karlo Mijares

# Uses a while loop to print out the
# subtracted number. When it reaches
# 0, the while loop breaks and prints
# out a message.

# Import sys
import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
    while True:
        print(timer)
        timer = timer - 1
        if timer == 0:
            print('blast off!')
            break
else:
    timer = 3
    while True:
        print(timer)
        timer = timer - 1
        if timer == 0:
            print('blast off!')
            break
