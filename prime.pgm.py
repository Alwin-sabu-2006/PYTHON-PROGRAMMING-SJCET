'''
Author=Alwin Sabu
description=a Python function that takes a number
 as a parameter and checks whether the number is prime or not
'''
def prime(n):
    l=True
    for i in range(2,n):
        if n%i==0:
            l=False
    if l==True:
        print("The number",n,"Is a PRIME NUMBER")
    else:
        print("The number", n, "Is not a PRIME NUMBER")
n=int(input("Enter the number:"))
prime(n)