'''
AUTHOR=ALWIN SABU
DATE=25/10/2024
DESCRIPTION= A PYTHON PROGRAM TO ACCEPT A NUMBER AND PRINT THE SUM OF ITS DIGITS
'''
num=int(input("Enter the number:"))
sum=0
while num>0:
    r=num%10
    sum=sum+r
    num=num//10
print("The sum of digits is",sum)