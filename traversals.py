# Inorder(Left,Root,Right)
# Preorder(Root,Left,Right)
# Postorder(Left,Right,Root)


def inOrder(arr,i):
    l = 2*i + 1
    r = 2*i + 2
    
    if len(arr) <= i:
        return
    inOrder(arr,l)
    print(arr[i], end = ' ')
    inOrder(arr,r)

def preOrder(arr,i):
    l = 2*i + 1
    r = 2*i + 2
    
    if len(arr) <= i:
        return
    print(arr[i], end = ' ')
    preOrder(arr,l)
    preOrder(arr,r)

def postOrder(arr,i):
    l = 2*i + 1
    r = 2*i + 2
    if len(arr) <= i:
        return
    postOrder(arr,l)
    postOrder(arr,r)
    print(arr[i], end = ' ')


arr = [1,2,3,4,5]

inOrder(arr,0)
print('')
preOrder(arr,0)
print('')
postOrder(arr,0)
print('')

