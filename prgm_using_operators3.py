'''
Author=Alwin Sabu
Date=18/10/24
Description=a Python program that demonstrates the usage of arithmetic, comparison,
 and logical operators. Perform a few operations and print the results.
'''
num1=int(input("enter the first number:"))
num2=int(input("enter the second number"))
add=num1+num2
div=num1/num2
print("Sum:",add,"Division:",div)
print("is a greater than b:",num1 > num2)
print("Are a and b equal:",num1 == num2)
print("LogicalAnd:",num1>0 and 0<num2)
print("LogicalOR:",num1>0 or num1<0)
