#!/usr/bin/env python3

#Antonio Karlo Mijares

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        t = int(number1) + int(number2)
        return t
    except:
        sumerror = 'error: could not add numbers'
        return sumerror
    
def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f=open(filename, 'r')
        f2read = f.readlines()
        return f2read

    except:
        fileerror = 'error: could not read file'
        return fileerror

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
