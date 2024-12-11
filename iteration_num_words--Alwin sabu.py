def iterate():
    l=[]
    for i in range(1,51):
        l.append (i)
    for w in l:
        if w%3==0 and w%5==0:
            print("FizzBuzz")
        
        elif w%3==0:
            print("Fizz")
        elif w%5==0:
            print("Buzz")
        else:
            print(w)
iterate()

