'''
Author=Alwin sabu
description=a Python function to find the maximum of three numbers
'''
def max_number(l):
    l.sort()
    print("The maximum value is:",l[2])
n1=int(input("Enter the  first number:"))
n2=int(input("Enter the second value:"))
n3=int(input("Enter the third value:"))
l=[n1,n2,n3]
max_number(l)