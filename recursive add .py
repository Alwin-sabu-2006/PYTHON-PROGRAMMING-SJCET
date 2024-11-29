def recursive_add(num1,num2):
    if num2==0:
        return num1
    else:
        return recursive_add(num1+1,num2-1)

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
f=recursive_add(num1,num2)
print(f)