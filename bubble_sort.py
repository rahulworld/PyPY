def bubbleSort(a):
    for passnum in range(len(a)-1,0,-1):
        for i in range(passnum):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

a = [54,26,93,17,77,31,44,55,20]
bubbleSort(a)
print(a)