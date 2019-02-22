#! /usr/bin/env python3
'''This check script will run the sample tests on assignment 1 script 
before submitting to blackboard by the students.
Please note that this script does not check the docstring of the script 
or its functions.

Released by Raymond Chan on Oct 30, 2018
'''

import types 
import sys
import os
import subprocess


def preliminary_grading(stud_name):
    message = '\n== Preliminary A1 Test Run Report for '+stud_name+'==\nThe following is your preliminary test run report for assignment 1. Please review the report and fix all the possible errors before submitting your python script and document files to blackboard using the assignment 1 submission link which will be available on Monday, February 18, 2019.\n'
    return message


if __name__ == '__main__':
   if len(sys.argv) != 2:
        student = input('Please enter your email user id:')
   else:
        student = sys.argv[1]
   
   a1_script = 'a1_'+student+'.py'
   if not os.path.isfile(a1_script):
        print('=' * 70)
        print('Your A1 script file',a1_script,'is not in the current direcoty')
        print('Please copy this script to the directory that contains your')
        print('A1 script file and run the this test run script again.')
        print('=' * 70)
        sys.exit()
   
   print(preliminary_grading(student))
   print('=' * 40)
   doc_marks = {} # data dictionary for documentation mark
   total_doc_marks = 0
   # test running student's script
   tests = { 1:['20180101 1','20180102'],
             2:['20180101 -1','20171231'],
             3:['20180101 2','20180103'],
             4:['--step 20180101 3','20180102\n20180103\n20180104\n'],
             5:['20180701 500','20191113'],
             6:['20189901 2','Error: wrong month entered'],
             7:['20180199 2','Error: wrong day entered'],
             8:['2018 2','Error: wrong date entered']
            }
   test_marks = {}
   for test_no in range(1,len(tests)+1):
       cmd = 'python3 a1_'+student+'.py '+tests[test_no][0]
       print('Test run command',test_no,':',cmd)
       p1 = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
       result = p1.communicate()[0].decode('utf-8').strip('\n')
       expected = tests[test_no][1].strip('\n')
       if result == expected:
          print('--test passed--')
          test_marks[test_no] = 1
       else:
          print('--test failed--')
          print('---- expect:',expected)
          print('----  given:',result)
          test_marks[test_no] = 0
   print('Test Results:',test_marks)
   total_test_marks = 0
   for item in test_marks:
       total_test_marks += test_marks[item] 
   total_test_marks = total_test_marks / 8 * 46
   print('Total test run marks: ',total_test_marks)
   grand_total = total_test_marks + total_doc_marks
   print('Total marks for script (max. 46):',grand_total)
