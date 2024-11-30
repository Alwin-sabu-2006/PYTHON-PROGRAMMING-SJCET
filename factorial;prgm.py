'''
Author=Alwin sabu
description=a Python function to calculate the factorial of a number
 (a non-negative integer). The function accepts the number as an argument.
'''

def factorial(n):

    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i

    print("The Factorial of the number", n, "is", factorial)
n= int(input("Enter the number:"))
if n>0:
    factorial(n)
else:
    print("Enter only positive number")
