#!/usr/bin/env python3

#Antonio Karlo Mijares

#Import os and sys
import os

def free_space():
	remaining = os.system("df -h | grep '/$' | awk '{print $4}'")
	utf = remaining[0].decode('utf-8').strip()
	print(remaining)
	

free_space()
