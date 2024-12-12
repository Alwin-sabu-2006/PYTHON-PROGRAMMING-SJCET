january=31
february=29
march=31
april=30
may=31
june=30
july=31
august=31
september=31
october=31
november=30
december=31
l=[january,february,march,april,may,june,july,august,september,october,november,december]
choice=input("Enter the name of the month:")
if choice.lower()=="january":
    print("No of days:",january)
if choice.lower()=="february":
    print("No of days:",february)
if choice.lower()=="march":
    print("No of days:",march)
if choice.lower()=="april":
    print("No of days:",april)
if choice.lower()=="may":
    print("No of days:",may)
if choice.lower()=="june":
    print("No of days:",june)
if choice.lower()=="july":

    print("No of days:",july)

if choice.lower()=="august":
    print("No of days:",august)


if choice.lower()=="september":
    print("No of days:",september)



if choice.lower()=="october":
    print("No of days:",october)


if choice.lower()=="november":
    print("No of days:",november)



if choice.lower()=="december":
    print("No of days:",december)

if choice not in l:
    print("Invalid Entry")



