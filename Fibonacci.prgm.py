'''
Author=Alwin sabu
Description=a Python program to generate the Fibonacci
sequence up to a specified number of terms.
Date=21/11/24
'''
n=int(input("Enter the number of terms in Fibonacci Series:"))
a=0
b=1
for i in range(0,n):
    print(a,end=" ")
    a,b=b,a+b

    
