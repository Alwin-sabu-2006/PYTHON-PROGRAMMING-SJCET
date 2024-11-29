def mobile_no():
    num1 = input("Enter the mobile number")
    if len(num1)==10 and num1[0] in '987':
        print(num1," is a Valid mobile number")
    else:
        print(num1," is an Invalid mobile number")
mobile_no()