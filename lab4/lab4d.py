#!/usr/bin/env python3 

# Antonio Karlo Mijares


# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(f_five):
    # Place code here - refer to function specifics in section below
    return f_five[0:5]

def last_seven(l_seven):
    # Place code here - refer to function specifics in section below
    return l_seven[-7:]

def middle_number(m_num):
    # Place code here - refer to function specifics in section below
    mint = str(m_num)
    m_string = mint[1:3]
    return m_string

def first_three_last_three(f_three, l_three):
    # Place code here - refer to function specifics in section below
    return f_three[0:3] + l_three[-3:]


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
