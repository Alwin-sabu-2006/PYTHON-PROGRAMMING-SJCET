'''
Author=Alwin Sabu
Description=This Python program identifies the longest word in a given list of words. It also calculates and displays the length of that word
'''
def longest_word(l):
    length=len(l[0])
    word=l[0]
    for i in l:
        if len(i)>length:
            length=len(i)
            word=i
            
    print("The longest word is:",word,"it's length is:",length)
l=[]
n=int(input("Enter the no of elements:"))
for w in range(n):
    b=input("Enter the elements:")
    l.append(b)
longest_word(l)
