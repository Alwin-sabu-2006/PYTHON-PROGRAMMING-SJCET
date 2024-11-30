'''
Author=Alwin sabu
description= a Python program to reverse a string
'''
def reverse(str):
    rstring=""
    index=len(str)
    while index>0:
        rstring=rstring+str[index-1]
        index=index-1
    print("The reverse of the string",str,"is",rstring)
str=input("Enter the string")
reverse(str)