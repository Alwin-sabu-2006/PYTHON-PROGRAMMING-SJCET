'''
Author=Alwin sabu
Description=Python program to find all pairs of numbers in a
list that add up to a specific sum,
without repeating the value in different order.
'''
def sum_list(l,sum):
    sum_list=[]
    for i in l:
        for k in l:
            if k+i==sum:
                sum_list.append((i,k))
    print(sum_list)
l=[]
n=int(input("Enter the no of elements:"))
for w in range(n):
    b=int(input("Enter the elements"))
    l.append(b)
sum=int(input("Enter the sum"))
sum_list(l,sum)
