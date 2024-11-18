'''
AUTHOR = ALWIN SABU
DESCRIPTION=a program to print the multiplication table of a given number using a while loop upto 10 times.The result can display using print() function.
DATE=17/11/24
'''
num=int(input("Enter number:"))
i=0
while i<11:
    num2=num*i
    print(num,"*",i,"=",num2)
    i=i+1
