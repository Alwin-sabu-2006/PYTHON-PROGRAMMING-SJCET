'''
AUTHOR=Alwin sabu
date=28/10/24
descriptioin= a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
'''
while True:
    print(" 1  Convert the Temperature to fahreheit \t 2. Convert the Temperature to celsius \t 3. Exit")
    ch=int(input("ENTER THE NUMBER OF THE OPTION THAT YOU WANT TO PERFORM:"))
    if ch==1:
        temp = float(input("Enter the temperature:"))
        t = (temp * (9 / 5)) + 32
        print(temp, "in Fahrenheit is", t)
    elif ch==2:
        temp = float(input("Enter the temperature:"))
        cel =  (temp - 32)*(5 / 9)
        print(temp, "in Celsius is", cel)
    elif ch==3:
        break
    else:
        print("INVALID ENTRY")


