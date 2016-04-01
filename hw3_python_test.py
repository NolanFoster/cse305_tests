#!/usr/bin/python
#!python
import hw3 ,filecmp, os

output_path = os.getenv('HOME') + '/Documents/CSE305/hw3/test_cases/output'
input_path = os.getenv('HOME') + '/Documents/CSE305/hw3/test_cases/input'

print("HW 2 Tests:")
for f in os.listdir(input_path+"/hw2"):
    if os.path.isfile(os.path.join(input_path+"/hw2", f)):
        hw3.hw3(input_path+"/hw2"+"/"+f,'output.txt')
    if(filecmp.cmp(output_path+"/"+f.replace('input', 'output'), 'output.txt')):
        print("            "+f+" : \033[1;32mPassed\033[0;0m")
    else:
        print("            "+f+" : \033[1;31mFailed\033[0;0m")
os.remove('output.txt')
print("HW 3 Tests:")
for f in os.listdir(input_path+"/hw3"):
    if os.path.isfile(os.path.join(input_path+"/hw3", f)):
        hw3.hw3(input_path+"/hw3"+"/"+f,f.replace('input', 'output'))
    if(filecmp.cmp(output_path+"/"+f.replace('input', 'output'), f.replace('input', 'output'))):
        print("            "+f+" : \033[1;32mPassed\033[0;0m")
        os.remove(f.replace('input', 'output'))
    else:
        print("            "+f+" : \033[1;31mFailed\033[0;0m")
