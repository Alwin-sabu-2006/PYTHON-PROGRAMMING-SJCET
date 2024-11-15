import random
#list slicing 
l1=[0,1,2,34,4]
print(l1[0])
#concatenation
l2=[90,56,78,43]
print(l1+l2)
#list multiplier
print(l1*2)
#
l=[]
for i in range(0,11):
    l.append(i)
for i in l:
    print(i,end=" ")

for i in l:
    l[5]=18
    print(i)
random_number_from_list=random.choice(l)
print(random_number_from_list)

