'''
AUTHOR=ALWIN SABU
DATE:25/10/24
DESCRIPTION:a Python program to find the largest of three numbers.
 The program should take three numbers as input from the user and
 determine which one is the largest.
Use conditional statements to compare the numbers.
'''
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if num1>num2:
    if num1>num3:
        print("The largest number is:",num1)
if num2>num1:
    if num2 > num3:
        print("The largest number is:", num2)
if num3>num1:
    if num3>num2:
        print("The largest number is:",num3)

