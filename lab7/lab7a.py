#!/usr/bin/env python3

# Antonio Karlo Mijares

# Store one IPv4 address
class IPAddress:
    # You probably want to construct it as a string, but you may want to store 
    # it as the four octets separately:
    def __init__(self, firstoct, secondoct, thirdoct, fourthoct):
    	self.firstoct  = firstoct
    	self.secondoct = secondoct
    	self.thirdoct = thirdoct
    	self.fourthoct = fourthoct
        
    # Is this address from a private subnet? e.g. starting with 192.168. 
    # or 10.
    #def isPrivate():