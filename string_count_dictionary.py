words="apple,orange,banana,apple,gauwa"
s=words.split(',')
word_count={}
for i in s:
    word_count[i]=word_count.get(i,0)+1
print(word_count)