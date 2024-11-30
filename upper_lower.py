'''
Author=Alwin Sabu
Description=a Python function that accepts a string
and counts the number of upper and lower case letters.
'''
def str_count(str):
    c=0
    u=0
    for i in str:
        if i.isupper():
            c=c+1
        if i.islower():
            u=u+1
    print("The no of upper case characters:",c)
    print("The no of lower case charactrs:",u)
str=input("Enter string:")
str_count(str)