'''
AUTHOR=ALWIN SABU
DESCRIPTION:A PRGM TO PRINT DIFFERENT PATTERNS USING LOOP
DAE=22/11/24
'''
num=int(input("Enter the no of rows:"))
for i in range(0,num+1):
    print("*"*i)



num1=int(input("Enter the no of Rows:"))
for j in range(num,0,-1):
    print("*"*j)


num2=int(input("Enter The no of rows:"))
for k in range(0,num+1):
    for y in range(num2-k):
        print(" ",end=" ")
    for t in range(k*2-1):
        print("*",end=" ")
    print()
