'''
Author=Alwin Sabu
description=a Python function that takes a list and
returns a new list with distinct elements from the first list.
'''
def new_list(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    print("The list with distinct elements are:",l1)
l=[]
n=int(input("Enter the number of elements in the list:"))
for w in range (n):
    b=int(input("Enter the elements:"))
    l.append(b)
new_list(l)