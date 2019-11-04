#Binary Search Tree
class Node:
    key = 0
    left = None
    right = None

def createNode(x):
    newNode = Node()
    newNode.key = x
    return newNode

def searchNode(root,x):
    if root == None or root.key == x:
        return root
    if root.key < x:
        return searchNode(root.right,x)
    return searchNode(root.left,x)

def insertNode(root,x):
    if root == None:
        return createNode(x)
    if x < root.key:
        root.left = insertNode(root.left,x)
    elif x > root.key:
        root.right = insertNode(root.right,x)
    return root

def deleteNode(root,x):
    if root == None:
        return root
    if x < root.key:
        root.left = deleteNode(root.left,x)
    elif x > root.key:
        root.right = deleteNode(root.right,x)
    else: ###x == root.key
        if root.left == None:
            temp = root.right
            del root
            return temp
        elif root.right == None:
            temp = root.left
            del root
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root
def minValueNode(root):
    current = root
    while current.left != None:
        current = current.left
    return current

#Create BST
def createTree(a,n):
    root = None
    for i in range(n):
        #print(a[i])
        root = insertNode(root,a[i])
    return root

def traversalTree(root):
    if root != None:
        traversalTree(root.left)
        print(root.key, end = ' ')
        traversalTree(root.right)
def size(root):
    if root == None:
        return 0
    return size(root.left) + 1 + size(root.right)

def deleteTree(root):
    if root == None:
        return
    deleteTree(root.left)
    deleteTree(root.right)
    del root
if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        n,m = map(int,input().split())
        lst = list(map(int,input().split()))
        tree = createTree(lst[0:n],n)
        for j in range(n,m+n,1):
            temp = size(tree)
            tree = insertNode(tree,lst[j])
            if size(tree) > temp:
                print('NO')
            else:
                print('YES')
        
