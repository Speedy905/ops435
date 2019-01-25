#!/usr/bin/env python3

#Antonio Karlo Mijares


def sum_numbers(number1, number2):
    addednum = int(number1) + int(number2)
    return addednum

def subtract_numbers(number1, number2):
    subtractednum = int(number1) - int(number2)
    return subtractednum

def multiply_numbers(number1, number2):
    multipliednum = int(number1) * int(number2)
    return multipliednum

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
