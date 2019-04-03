#!/usr/bin/env python3
import os
import sys
import time
import argparse
#if temp[4] == timeList1[0][0] and temp[5] == timeList1[0][1]:
user = 'rchan'
timeList1 = []
timeList2 = []
n = 0
filelist = 'usage_data_file'
file = open(filelist, 'r')
fileRead = file.readlines()
fileRead = fileRead[1::]
for eachRecond in fileRead:
    temp = fileRead[n].split()
    n = n + 1
    if temp[0] == user:
        timeList1.append(temp[4:8])
        timeList2.append(temp[10:14])
a = 0
j = 0
List2 = []
List1 = []
for EachObject in timeList2:
    TimeTemp = sum(x * int(t) for x, t in zip([3600, 60, 1], timeList2[a][2].split(":")))
    List1.append(TimeTemp)
    a = a + 1

for EachObject in timeList1:
    TimeTemp = sum(x * int(t) for x, t in zip([3600, 60, 1], timeList1[j][2].split(":")))
    List2.append(TimeTemp)
    j = j + 1

A1 = 0
A2 = []
for each in List1:
    math1 = List1[A1] - List2[A1]
    A2.append(math1)
    A1 = A1 + 1

FinalMath = sum(A2)
print(fileRead[0][69:89])
print('temp:',temp)
print('timelist1: ',timeList1)
print('timelist2: ',timeList2)
print('Lis1:',List1)
print('Lis2:',List2)
print(A2)
print(FinalMath)