def selectionSort(a):
   for fillslot in range(len(a)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if a[location]>a[positionOfMax]:
               positionOfMax = location

       temp = a[fillslot]
       a[fillslot] = a[positionOfMax]
       a[positionOfMax] = temp

a = [54,26,93,17,77,31,44,55,20]
selectionSort(a)
print(a)
