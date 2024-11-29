def sides():
    s1 = int(input("Enter the first side of the triangle:"))
    s2 = int(input("Enter the second side of the triangle:"))
    s3 =int(input("Enter the third side of the triangle:"))
    l1=[s1,s2,s3]
    l1.sort()
    if l1[2]**2==l1[1]**2+l1[0]**2:
        print("It is a Right Angled Triangle")
    else:
        print("It is not an Right Angled Triangle")
sides()