import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print("Traversing this 2d array")
for i in arr:
    for w in i:
        print(w,end=" ")
    print()