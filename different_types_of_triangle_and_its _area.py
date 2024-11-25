'''
Author=Alwin Sabu
Date=25/11/24
description=:Python program calculates the area of a triangle
and determines its type:Isosceles, Equilateral, or Scalene (different sides).
'''
import math
n1=int(input("Enter the value of first side of the triangle:"))
n2=int(input("Enter the value of second side of the the triangle:"))
n3=int(input("Enter the value of third side of the Triangle:"))
area=s=(n1+n2+n3)/2
area=math.sqrt(s*(s-n1)*(s-n2)*(s-n3))
print("Area of the Triang;e is:",area)
if n1==n2==n3:
    print("The triangle is:Equilateral")
if n1==n2!=n3 or n1==n3!=n2 or n2==n3!=n1:
    print("The triangle is:Isoceles")
if n1!=n2!=n3!=n1:
    print("The Triangle is :Scalene")
