'''
Author==Alwin sabu
Description=
Python program to construct the following pattern, using a nested for loop.
'''

num2=int(input("Enter the no of rows"))
for i in range (1,num2+1):
    print("*\t"*i)
for i in range(num2,0,-1):
    print("*\t"*i)
