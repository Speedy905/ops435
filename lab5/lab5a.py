#!/usr/bin/env python3

#Antonio Karlo Mijares

def read_file_string(file_name):
    # Takes a filename string, returns a string of all lines in the file
    f = open(file_name, 'r')
    read = f.read()
    return read


def read_file_list(file_name):
    # Takes a filename string, returns a list of lines without new-line characters
    f2 = open(file_name, 'r')
    f2read = f2.read()
    linesplit = f2read.splitlines()
    return linesplit

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
