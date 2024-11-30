'''
Author=Alwin sabu
descripton=a Python function to multiply all the numbers in a list
'''
def mul(l):
    mul=1
    for i in l:
         mul=mul*i
    print("The sum of the elements in the list is:",mul)
l=[]
n=int(input("Enter the number of elements in the list"))
for w in range (n):
    b=int(input("Enter the elements:"))
    l.append(b)
mul(l)