#!/usr/bin/python
#!python
import filecmp, os, sys
from subprocess import DEVNULL, STDOUT, check_call
path = os.getenv('HOME') + '/Documents/CSE305/hw3/'
sys.path.insert(0, path+'/python')
import hw3
output = False
def python_test(hw):
    passed=0
    total=0
    failed = 0
    for f in os.listdir(path+"test_cases/input/"+hw):
        total=total+1
        if os.path.isfile(os.path.join(path+"test_cases/input/"+hw, f)):
            try:
                hw3.hw3(path+"test_cases/input/"+hw+"/"+f,'python_'+f.replace('input', 'output'))
            except:
                print ("Unexpected error:", sys.exc_info())

        if(filecmp.cmp(path+"test_cases/output/"+f.replace('input', 'output'), 'python_'+f.replace('input', 'output'))):
            passed=passed+1
            if output:
                print("            "+f+" : \033[1;32mPassed\033[0;0m")
            os.remove('python_'+f.replace('input', 'output'))
        else:
            failed=failed+1
            if output:
                print("            "+f+" : \033[1;31mFailed\033[0;0m")
    print('\033[1;32m'+str(passed)+"\033[0;0m"+' \033[1;37mtests passed of '+str(total)+'\033[0;0m')

def java_test(hw):
    passed=0
    total=0
    failed = 0
    check_call(['javac', 'tester.java'],stdout=DEVNULL, stderr=STDOUT)
    for f in os.listdir(path+"test_cases/input/"+hw):
        total=total+1
        if os.path.isfile(os.path.join(path+"test_cases/input/"+hw, f)):
            try:
                check_call(['java', 'tester', path+"test_cases/input/"+hw+"/"+f, 'java_'+f.replace('input', 'output')],  stdout=DEVNULL, stderr=STDOUT)
            except:
                print ("Unexpected error:", sys.exc_info())

        if(filecmp.cmp(path+"test_cases/output/"+f.replace('input', 'output'), 'java_'+f.replace('input', 'output'))):
            passed=passed+1
            if output:
                print("            "+f+" : \033[1;32mPassed\033[0;0m")
            os.remove('java_'+f.replace('input', 'output'))
        else:
            if output:
                print("            "+f+" : \033[1;31mFailed\033[0;0m")

    os.remove('tester.class')
    os.remove('hw3.class')
    print('\033[1;32m'+str(passed)+'\033[0;0m \033[1;37mtests passed of ' +str(total)+'\033[0;0m')

def sml_test(hw):
    passed=0
    total=0
    failed = 0
    for f in os.listdir(path+"test_cases/input/"+hw):
        total=total+1
        if os.path.isfile(os.path.join(path+"test_cases/input/"+hw, f)):
            try:
                check_call(['sml', 'tester.sml', path+"test_cases/input/"+hw+"/"+f, 'sml_'+f.replace('input', 'output')], stdout=DEVNULL, stderr=STDOUT)
            except:
                print ("Unexpected error:", sys.exc_info())

        if(filecmp.cmp(path+"test_cases/output/"+f.replace('input', 'output'), 'sml_'+f.replace('input', 'output'))):
            passed=passed+1
            if output:
                print("            "+f+" : \033[1;32mPassed\033[0;0m")
            os.remove('sml_'+f.replace('input', 'output'))
        else:
            if output:
                print("            "+f+" : \033[1;31mFailed\033[0;0m")
    print('\033[1;32m'+str(passed)+'\033[0;0m \033[1;37mtests passed of ' +str(total)+'\033[0;0m')

print('\033[1;33m'+"HW 2 Python Tests:"+'\033[0;0m')
python_test("hw2")


print('\033[1;33m'+"HW 3 Python Tests:"+'\033[0;0m')
python_test("hw3")


print('\033[1;35m'+"HW 2 Java Tests:"+'\033[0;0m')
java_test("hw2")

print('\033[1;35m'+"HW 3 Java Tests:"+'\033[0;0m')
java_test("hw3")


print('\033[1;31m'+"HW 2 SML Tests:"+'\033[0;0m')
sml_test("hw2")


print('\033[1;31m'+"HW 3 SML Tests:"+'\033[0;0m')
sml_test("hw3")
