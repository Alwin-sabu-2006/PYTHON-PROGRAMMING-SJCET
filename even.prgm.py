'''
Author=Alwin Sabu
description=a Python program to print the even numbers from a given list.
'''
def even(l):
    l2=[]
    for i in l:
        if i%2==0:
            l2.append(i)
    print(l2)

l=[]
n=int(input("Enter the number of elements in the list"))
for w in range (n):
    b=int(input("Enter the elements:"))
    l.append(b)
even(l)