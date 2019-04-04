#!/bin/bash

# data file: a2_test_data_2
echo "Test data file: a2_test_data_2"

cat a2_test_data_2

./ur.py -h

./ur.py -l user a2_test_data_2
./ur.py -l host a2_test_data_2
./ur.py -u user5 -t daily a2_test_data_2
./ur.py -u user5 -t weekly a2_test_data_2
./ur.py -u user5 -t monthly a2_test_data_2
./ur.py -r 173.32.126.71 -t daily a2_test_data_2
./ur.py -r 173.32.126.71 -t weekly a2_test_data_2
./ur.py -r 173.32.126.71 -t monthly a2_test_data_2

./ur.py -l user a2_test_data_2 -v
./ur.py -l host a2_test_data_2 -v
./ur.py -u user5 -t daily a2_test_data_2 -v
./ur.py -u user5 -t weekly a2_test_data_2 -v
./ur.py -u user5 -t monthly a2_test_data_2 -v
./ur.py -r 173.32.126.71 -t daily a2_test_data_2 -v
./ur.py -r 173.32.126.71 -t weekly a2_test_data_2 -v
./ur.py -r 173.32.126.71 -t monthly a2_test_data_2 -v
