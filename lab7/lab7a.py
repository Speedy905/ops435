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
class BMWModel:
    def __init__(self, model):
        self.model = model

    # Price range
    # Determine the price range of model
    def pricerange(self):
        if self.model == "2":
            return "The BMW " + str(self.model) + " Series Model is between 35K to 60K (USD)"
        elif self.model == "3":
            return "The BMW " + str(self.model) + " Series Model is between 40K to 45K (USD)"
        elif self.model == "4":
            return "The BMW " + str(self.model) + " Series Model is between 52K to 72K (CAD)"
        elif self.model == "X":
            return "The BMW " + str(self.model) + " Series Model is between 60K to 76K (USD)"
        elif self.model == "M":
            return "The BMW " + str(self.model) + " Series Model is between 47K to 120K (CAD)"
        elif self.model == "i":
            return "The BMW " + str(self.model) + " Series Model is between 50K to 100K (CAD)"

# Store information about a specific car that someone owns.
# Spend some time thinking why this class is different than the one above, 
#and whether it has to be different:
class Car:
    def __init__(self, name, colour, brand, vin):
        self.name = name
        self.brand = brand
        self.colour = colour
        self.vin = vin

    # Display car info
    def printcar(self):
        print ("Name: " + str(self.name))
        print ("Car Brand: " + str(self.brand))
        print ("Car Colour: " + str(self.colour))
        print ("VIN Number: " + str(self.vin))

if __name__ == '__main__':
    addr1 = IPAddress(192, 168, 1, 3)
    addr2 = IPAddress(192, 168, 1, 10)
    addr3 = IPAddress(10, 0, 0, 50)
    addr4 = IPAddress(142, 204, 1, 2)
    name1 = Person("Andrew", "Oatley-Willis")
    name2 = Person("Murray", "Saul")
    name3 = Person("Andrew", "Smith")
    bmw1 = BMWModel("2")
    bmw2 = BMWModel("3")
    bmw3 = BMWModel("4")
    bmw4 = BMWModel("X")
    bmw5 = BMWModel("M")
    bmw6 = BMWModel("i")
    car1 = Car("Andrew", "Silver", "Civic", 123456789)
    car2 = Car("John", "Blue", "Subaru", "0987654321")
    car3 = Car("Evan", "Silver", "BMW M Series", 4567891230)


    print('')
    print(addr1.isPrivate())
    print(addr2.isPrivate())
    print(addr3.isPrivate())
    print(addr4.isPrivate())
    print ('')
    print(name1.printname())
    print(name2.printname())
    print(name3.printname())
    print('')
    print(bmw1.pricerange())
    print(bmw2.pricerange())
    print(bmw3.pricerange())
    print(bmw4.pricerange())
    print(bmw5.pricerange())
    print(bmw6.pricerange())
    print('')
    car1.printcar()
    print('')
    car2.printcar()
    print('')
    car3.printcar()