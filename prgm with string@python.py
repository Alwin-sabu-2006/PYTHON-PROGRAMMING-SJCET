'''
Author=ALWIN SABU
DATE=19/10/24
DESCRIPTION=a Python program that performs the following tasks:
 Create, concatenate, and print a string and access a sub-string from a given string
'''
str1=input("Enter your first name:")
str2=input("Enter your last name:")
result=str1+" "+str2
print(result)
l=len(str1)+1
last_str=result[:l]
print(last_str)
