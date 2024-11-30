'''
Author=Alwin sabu
description=Python function to sum all the numbers in a list.
'''
def add(l):
    sum=0
    for i in l:
         sum=sum+i
    print("The sum of the elements in the list is:",sum)
l=[]
n=int(input("Enter the number of elements in the list"))
for w in range (n):
    b=int(input("Enter the elements:"))
    l.append(b)
add(l)