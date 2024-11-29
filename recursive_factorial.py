def factorial(n):
    if n==0:
        return 1
    else:
         return  n*(factorial(n-1))
n=int(input("Enter The number"))
f=factorial(n)
print("The factorial of the number",n,"is",f)

