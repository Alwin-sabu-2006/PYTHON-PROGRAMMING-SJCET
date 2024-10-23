'''
Author=ALWIN SABU
DATE=19/10/2024
DESCRIPTION=Simple desktop calculator using Python.

'''
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
#add
Add=num1+num2
print("the sum of num1 and num2 is:",Add)
#Sub
sub=num2-num1
print("The difference when num1 is subtracted from num2 is:",sub)
#multiply
mul=num1*num2
print("The product of num1 and num2 is:",mul)
#div
div=num1/num2
print("The quotient when num1 is divided by num2 is",div)
#modulus
mod=num1%num2
print("The remainder when num 1 is divided by num2 is",mod)
#combine
result=(num1+num2)*num3/2
print("The result of (num1+num2)*num3/2 is",result)

