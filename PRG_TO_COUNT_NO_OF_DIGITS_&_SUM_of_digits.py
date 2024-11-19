'''
Author= Alwin Sabu
DESCRIPTION=a program to count the number of digits in a given
integer using a while loop.And Display the sum of digits.
DATE=19/11/24
'''
n=int(input("ENTER THE NUMBER:"))
sum=0
count=0
while n>0:
   re=n%10
   sum=sum+re
   count=count+1
   n=n//10
print("The sum of the digits is:",sum)
print("The number of digits:",count)
    
