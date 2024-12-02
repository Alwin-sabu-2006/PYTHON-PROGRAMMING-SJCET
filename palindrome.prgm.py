def palindrome(str):
    for i in str:
        c=str[-1::-1]
    print(c)
    if c==str:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

str=input("Enter the string:")
palindrome(str)
