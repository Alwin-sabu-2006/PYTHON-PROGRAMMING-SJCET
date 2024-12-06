def recursive_multiply(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+recursive_multiply(num1,num2-1)

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
f=recursive_multiply(num1,num2)
print(f)