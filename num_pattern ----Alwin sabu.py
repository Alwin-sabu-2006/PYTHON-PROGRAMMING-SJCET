'''
Author=Alwin Sabu
Description=
:Python program to construct the following pattern, using a nested loop number.
Input:
enter the rows: 9

Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''

num=int(input("Enter the no of rows"))
for i in range (1,num+1):
    print(str(i)*i)
