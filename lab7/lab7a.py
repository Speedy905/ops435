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
    def isPrivate(self):
        if self.fourthoct == 0 or self.fourthoct == 255:
            return "This is a private address"
        else:
            return "Not a private address"

# Store information about a person, perhaps someone you'll be adding as a user to a system:
class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        return "Name = " + str(self.firstname) + " " + str(self.lastname)
    

# Store information about different models from a specific manufacturer. 
#Perhaps how many seats they have and how much fuel they use and the price range:
# Doesn't have to be BMW, pick any car or bike manufacturer:
#class BMWModel:
    

# Store information about a specific car that someone owns.
# Spend some time thinking why this class is different than the one above, 
#and whether it has to be different:
#class Car:

if __name__ == '__main__':
    addr1 = IPAddress(192, 168, 1, 3)
    addr2 = IPAddress(192, 168, 1, 10)
    addr3 = IPAddress(10, 0, 0, 50)
    addr4 = IPAddress(142, 204, 1, 2)
    name1 = Person("Andrew", "Oatley-Willis")
    name2 = Person("Murray", "Saul")
    name3 = Person("Andrew", "Smith")

    print(addr1.isPrivate())
    print(addr2.isPrivate())
    print(addr3.isPrivate())
    print(addr4.isPrivate())
    print ('')
    print(name1.printname())
    print(name2.printname())
    print(name3.printname())