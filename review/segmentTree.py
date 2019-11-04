#Build a segment tree

def buildTree(a, segtree, left, right, index):
	if left == right:
		segtree = a[left]
		return 

	mid = (left + right) // 2
	buildTree(a, segtree, left, mid, 2*index + 1)
	buildTree(a, segtree, mid + 1, right, 2*index + 2)
	segtree[index] = min(segtree[2*index+1], segtree[2*index+2])


