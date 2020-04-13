import random

def swap(arr,l,r):
    k = arr[l]
    arr[l] = arr[r]
    arr[r] = k
    return arr

def partition(arr,l,r):
    i = l -1
    j = l
    pivot = arr[r]
    print(pivot,r)
    for n in range(l,r+1):
        if arr[j] <= pivot:
            i += 1
            arr = swap(arr,i,j)
        j += 1
    return i

def quicksort(arr,l,r):
    if l < r:
        p = partition(arr,l,r)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,r)
    return arr




a = [40,20,30,10,70,50,60]#,80,90,100]
a2 = [4,2,1,5,6,3]
arr = quicksort(a,0,len(a)-1)
print(arr)

