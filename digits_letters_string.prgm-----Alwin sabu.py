def string_cal(str):
    c=0
    d=0
    for i in str:
        if i.isalpha():
            c=c+1
        if i.isdigit():
            d=d+1
    print("The no of letters:",c)
    print("The no of digits:",d)
str=input("Enter the string:")
string_cal(str)
