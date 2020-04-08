def binarySearchHelper(arr,l,r,x):
    if(l == r):
        if arr[l] == x:
            return l
        else:
            print("item not found")
            return None
    else:
        m = (l+r)//2
        if arr[m] == x:
            return m
        elif x < arr[m]:
            return binarySearchHelper(arr,l,m-1,x)
        else:
            return binarySearchHelper(arr,m+1,r,x)

def binarySearch(array,value):
    return binarySearchHelper(array,0, len(array)-1,value)



a = [1,2,3,5,6,8,9,10,18,22,23,25,29,34] 
inx = binarySearch(a,22)
print("idx -> ",inx, end=' ')
if inx != None:
    print(a[inx])
else:
    print('\n')