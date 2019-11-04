#Trie
class Node:
    countLeaf = 0
    child = dict()
    def __init__(self):
        self.countLeaf = 0
        self.child = dict()

def addWord(root,s,w):
    tmp = root
    for ch in s:
        if ch in tmp.child:
            tmp = tmp.child[ch]
        else:
            tmp.child[ch] = Node()
            tmp = tmp.child[ch]
            if tmp.countLeaf < w:
                tmp.countLeaf = w

def findWord(root,s):
    tmp = root
    count = 0
    for ch in s:
        #print(ch)
        if ch not in tmp.child:
            return False
        count += 1
        tmp = tmp.child[ch]
    max_value = 0
    for sub_ch in tmp.child.keys():
        if tmp.child[sub_ch].countLeaf > max_value:
            max_value = tmp.child[sub_ch].countLeaf
    return max_value

def isWord(node):
    return node.countLeaf != 0

def isEmpty(node):
    return len(node.child) == 0

def removeWord(root,s,level,len):
    if root == None:
        return False
    if level == len:
        if root.countLeaf > 0:
            root.countLeaf -= 1
            return True
        return False
    ch = s[level]
    flag = removeWord(root.child[ch],s,level + 1, len)
    if flag == True and isWord(root.child[ch]) == False and isEmpty(root.child[ch]) == True:
        tmp = root.child[ch]
        del tmp
        del root.child[ch]
    return flag

if __name__ == '__main__':
    n, q = map(int,input().split())
    trie = Node()
    for i in range(n):
        s, w = input().split()
        addWord(trie, s, int(w))
    for j in range(q):
        st = input()
        result = findWord(trie,st)
        if result > 0:
            print(result)
        else:
            print(-1)
