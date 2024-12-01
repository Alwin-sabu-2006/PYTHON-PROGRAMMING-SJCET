'''
Author=Alwin sabu
description: Python function to check whether a number is "Perfect" or not
'''

def perfect(n):
    l=[]
    sum=0
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    for w in l:
        sum=sum+w
    if sum==n:
        print("The given number",n,"is a perfect number")
    else:
        print("The given number",n,"is not a perfect number")
n=int(input("Enter the number:"))
perfect(n)
