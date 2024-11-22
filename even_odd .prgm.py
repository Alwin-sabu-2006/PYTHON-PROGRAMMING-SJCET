l1=[]
n=int(input("Enter the no of elements in list1:"))
for i in range(n):
    b=int(input("Enter the elements"))
    l1.append(i)
l2=[]
d=int(input("Enter the no f elements in the list 2:"))
for j in range(d):
    t=int(input("Enter the elements:"))
    l2.append(t)
l3=l1+l2
even_list=[]
odd_list=[]
for i in l3:
    if i%2==0:
        even_list.append(i)

    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
l6=[]
l6=even_list+odd_list
print(l1)
print(l2)
print(l6)
