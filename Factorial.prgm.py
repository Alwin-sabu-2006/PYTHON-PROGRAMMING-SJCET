'''
AUTHOR=ALWIN SABU
DESCRIPTION=a Python program to calculate the factorial of a given number
DATE=20/11/24
'''
N=int(input("Enter the number:"))
factorial=1
for i in range(1,N+1):
    factorial=factorial*i
print("The Factorial of the number",N,"is",factorial)    
