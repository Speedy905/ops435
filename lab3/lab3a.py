#!/usr/bin/env python3

#Antonio Karlo Mijares

# return_text_value function
def return_text_value():
	name = 'Terry'
	greeting = 'Good Morning ' + name
	return greeting

# return_number_value function
def return_number_value():
	num1 = 10
	num2 = 5
	num3 = num1 + num2
	return num3
	
# Main program
if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))
