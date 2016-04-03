#!/usr/bin/python
#!python
import hw3 ,filecmp, os, sys

path = os.getenv('HOME') + '/Documents/CSE305/hw3/'

def python_test(hw):
    for f in os.listdir(path+"test_cases/input/"+hw):
        if os.path.isfile(os.path.join(path+"test_cases/input/"+hw, f)):
            try:
                hw3.hw3(path+"test_cases/input/"+hw+"/"+f,f.replace('input', 'output'))
            except:
                print ("Unexpected error:", sys.exc_info())

        if(filecmp.cmp(path+"test_cases/output/"+f.replace('input', 'output'), f.replace('input', 'output'))):
            print("            "+f+" : \033[1;32mPassed\033[0;0m")
            os.remove(f.replace('input', 'output'))
        else:
            print("            "+f+" : \033[1;31mFailed\033[0;0m")

print("HW 2 Tests:")
python_test("hw2")

print("HW 3 Tests:")
python_test("hw3")
