#!/bin/bash

# data file: a2_test_data_0
echo "Test data file: a2_test_data_0"

cat a2_test_data_0

./ur.py -h

./ur.py -l user a2_test_data_0
./ur.py -l host a2_test_data_0
./ur.py -u rchan -t daily a2_test_data_0
./ur.py -u rchan -t weekly a2_test_data_0
./ur.py -u rchan -t monthly a2_test_data_0
./ur.py -r 10.40.105.130 -t daily a2_test_data_0
./ur.py -r 10.40.105.130 -t weekly a2_test_data_0
./ur.py -r 10.40.105.130 -t monthly a2_test_data_0

./ur.py -l user a2_test_data_0 -v
./ur.py -l host a2_test_data_0 -v
./ur.py -u rchan -t daily a2_test_data_0 -v
./ur.py -u rchan -t weekly a2_test_data_0 -v
./ur.py -u rchan -t monthly a2_test_data_0 -v
./ur.py -r 10.40.105.130 -t daily a2_test_data_0 -v
./ur.py -r 10.40.105.130 -t weekly a2_test_data_0 -v
./ur.py -r 10.40.105.130 -t monthly a2_test_data_0 -v
