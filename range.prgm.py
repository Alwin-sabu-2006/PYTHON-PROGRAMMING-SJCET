def test(n):
    list=[]
    for i in range(0,9+1):
        list.append(i)
    if n in list:
            print(" The number",n,"is not Present")
    else:
            print("The number ",n," is Not present  ")
n=int(input("Enter the number:"))
test(n)