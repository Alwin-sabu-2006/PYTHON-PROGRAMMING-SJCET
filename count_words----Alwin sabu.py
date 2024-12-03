'''
Author=Alwinsabu
Description=Python program counts the frequency of each word in a
given sentence. It takes a sentence as input, processes
the text, and displays how many times each word appears
'''



def count_sentence(str):
    w=str.split(" ")
    l=set(w)
    for i in l:
        count=0
        for j in w:
            if i==j:
                count=count+1
        print(i,':',count)
    
        
        
        
        
str=input("Enter the sentence")
count_sentence(str)
        
    
