def merge(l,r):
    k=j=0
    rtnArr =[]
    for i in range(0,len(l)+len(r)):
        if j != len(r) and k != len(l):
            if l[k] > r[j]:
                rtnArr.append(r[j])
                j+=1
            else:
                rtnArr.append(l[k])
                k+=1
        elif j == len(r) and k != len(l):
            rtnArr.append(l[k])
            k += 1
        elif j != len(r) and k == len(l):
            rtnArr.append(r[j])
            j += 1
    return rtnArr

def mergesort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]
    print(mid)
    print("l -> ",l)
    print("r -> ",r)
    l = mergesort(l)
    r = mergesort(r)
    print("merge -> ", merge(l,r))
    return merge(l,r)



a = [9,8,7,6,5,4,3,2,1,0]
mergesort(a)
