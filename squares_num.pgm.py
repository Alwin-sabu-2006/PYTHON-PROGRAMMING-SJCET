def square(l):
    l1=[]
    for i in l:
        i=i**2
        l1.append(i)
        
    print("The list with the squares of the numbers=",l1)
l=[]
for w in range(1,30+1):
    l.append(w)
print("Initial list",l)
square(l)
