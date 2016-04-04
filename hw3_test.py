#!/usr/bin/python
#!python
import filecmp, os, sys
path = os.getenv('HOME') + '/Documents/CSE305/hw3/'
sys.path.insert(0, path+'/python')
import hw3

def python_test(hw):
    for f in os.listdir(path+"test_cases/input/"+hw):
        if os.path.isfile(os.path.join(path+"test_cases/input/"+hw, f)):
            try:
                hw3.hw3(path+"test_cases/input/"+hw+"/"+f,'python_'+f.replace('input', 'output'))
            except:
                print ("Unexpected error:", sys.exc_info())

        if(filecmp.cmp(path+"test_cases/output/"+f.replace('input', 'output'), 'python_'+f.replace('input', 'output'))):
            print("            "+f+" : \033[1;32mPassed\033[0;0m")
            os.remove('python_'+f.replace('input', 'output'))
        else:
            print("            "+f+" : \033[1;31mFailed\033[0;0m")

def java_test(hw):
    os.system('javac tester.java')
    for f in os.listdir(path+"test_cases/input/"+hw):
        if os.path.isfile(os.path.join(path+"test_cases/input/"+hw, f)):
            try:
                os.system('java tester ' + path+"test_cases/input/"+hw+"/"+f+' '+'java_'+f.replace('input', 'output'))
            except:
                print ("Unexpected error:", sys.exc_info())

        if(filecmp.cmp(path+"test_cases/output/"+f.replace('input', 'output'), 'java_'+f.replace('input', 'output'))):
            print("            "+f+" : \033[1;32mPassed\033[0;0m")
            os.remove('java_'+f.replace('input', 'output'))
        else:
            print("            "+f+" : \033[1;31mFailed\033[0;0m")

    os.remove('tester.class')
    os.remove('hw3.class')

print("HW 2 Python Tests:")
python_test("hw2")
print("HW 2 Java Tests:")
java_test("hw2")

print("HW 3 Tests:")
python_test("hw3")
