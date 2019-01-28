#!/usr/bin/env python3

#Antonio Karlo Mijares

# Operate funciton
# It checks the number of arguments
# If it is less than 3, it prints out an error
# If not, it goes to the 2nd logic statements
# If the 3rd value in array does matches the values 
# It executes the function
# Else it prints out an error
def operate(number1, number2, operator):
	checkingarguments = [number1, number2, operator]
	if (len(checkingarguments)) == 3:
		if checkingarguments[2] == 'add':
			sum = number1 + number2
			return sum
		elif checkingarguments[2] == 'subtract':
			subtraction = number1 - number2
			return subtraction
		elif checkingarguments[2] == 'multiply':
			multiplication = number1 * number2
			return multiplication
		else:
			return 'Error: function operator can be "add", "subtract", or "multiply"'
	else:
		return 'Need 3 arguments'

if __name__ == '__main__':
	print(operate(10, 5, 'add'))
	print(operate(10, 4, 'subtract'))
	print(operate(10, 5, 'multiply'))
	print(operate(10, 5, 'divide'))
