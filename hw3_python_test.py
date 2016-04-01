#!/usr/bin/python
#!python
import hw3 ,filecmp, os

path = os.getenv('HOME') + '/Documents/CSE305/hw3/'
output_path = os.getenv('HOME') + '/Documents/CSE305/hw3/test_cases/output'
input_path = os.getenv('HOME') + '/Documents/CSE305/hw3/test_cases/input'

print("HW 2 Tests:")
for f in os.listdir(path+"test_cases/input/hw2"):
    if os.path.isfile(os.path.join(path+"test_cases/input/hw2", f)):
        hw3.hw3(path+"test_cases/input/hw2"+"/"+f,'output.txt')
    if(filecmp.cmp(path+"test_cases/output/"+f.replace('input', 'output'), 'output.txt')):
        print("            "+f+" : \033[1;32mPassed\033[0;0m")
    else:
        print("            "+f+" : \033[1;31mFailed\033[0;0m")
os.remove('output.txt')
print("HW 3 Tests:")
for f in os.listdir(path+"test_cases/input/hw3"):
    if os.path.isfile(os.path.join(path+"test_cases/input/hw3", f)):
        hw3.hw3(path+"test_cases/input/hw3"+"/"+f,f.replace('input', 'output'))
    if(filecmp.cmp(path+"test_cases/output/"+f.replace('input', 'output'), f.replace('input', 'output'))):
        print("            "+f+" : \033[1;32mPassed\033[0;0m")
        os.remove(f.replace('input', 'output'))
    else:
        print("            "+f+" : \033[1;31mFailed\033[0;0m")
