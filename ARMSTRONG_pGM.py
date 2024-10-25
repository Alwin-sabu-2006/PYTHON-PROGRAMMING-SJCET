'''
AUTHOR=ALWIN SABU
DATE=25/10/24
DESCRIPTION=A python program to check whether a given no is armstrong number
'''
num=int(input("Enter the number:"))
t=num
AD=0
while num>0:
    r=num%10
    cu=r**3
    AD=AD+cu
    num=num//10
if AD==t:
    print(t,"is an armstrong number")
else:
    print(t,"is not an armstrong number")