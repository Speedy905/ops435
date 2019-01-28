#!/usr/bin/env python3

#Antonio Karlo Mijares

#Import os
import os

def free_space():
	remaining = os.popen("df -h | grep '/$' | awk '{print $4}'").read().strip()
	return remaining
	

print(free_space())
