'''
AUTHOR=ALWIN SABU
DATE=25/10/2024
Description=a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c5=f−329
'''
tem=float(input("Enter The Temperature:"))
temp=input("Is this in (C)elsius or (F)ahrenheit:")
if temp=='C':
    t=(tem*(9/5))+32
    print(tem ,"in Fahrenheit is",t)
if temp=="F":
    cel=(5/9)*(tem-32)
    print(tem,"in Celsius is",cel)
