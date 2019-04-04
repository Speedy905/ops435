#!/bin/bash

# data file: a2_test_data_1
data_file=a2_test_data_1
echo "Test data file: ${data_file}"

cat ${data_file}

./ur.py -h

./ur.py -l user ${data_file}
./ur.py -l host ${data_file}
./ur.py -u user4 -t daily ${data_file}
./ur.py -u user4 -t weekly ${data_file}
./ur.py -u user4 -t monthly ${data_file}
./ur.py -r 173.32.126.71 -t daily ${data_file}
./ur.py -r 173.32.126.71 -t weekly ${data_file}
./ur.py -r 173.32.126.71 -t monthly ${data_file}

./ur.py -l user ${data_file} -v
./ur.py -l host ${data_file} -v
./ur.py -u user4 -t daily ${data_file} -v
./ur.py -u user4 -t weekly ${data_file} -v
./ur.py -u user4 -t monthly ${data_file} -v
./ur.py -r 173.32.126.71 -t daily ${data_file} -v
./ur.py -r 173.32.126.71 -t weekly ${data_file} -v
./ur.py -r 173.32.126.71 -t monthly ${data_file} -v
