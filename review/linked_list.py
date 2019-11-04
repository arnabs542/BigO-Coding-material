class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next 

	def __str__(self):
		return str(self.cargo)


def print_list(node):
	while node is not None:
		print(node, end=' ')
		node = node.next
	print()


def print_backward(list_head):
	if list_head is None:
		return 
	head = list_head 
	tail = list_head.next
	print_backward(tail)
	print(head, end=' ')


if __name__ == '__main__':
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node1.next = node2
	node2.next = node3

	print('Node 1 cargo: {0} and is linked to node {1}'.format(node1, node1.next))
	print('Node 2 cargo: {0} and is linked to node {1}'.format(node2, node2.next))
	print('Node 3 cargo: {0} and is linked to node {1}'.format(node3, node3.next))

	print('List traversal')
	print_list(node1)

	print('Print backward')
	print_backward(node1)
	print()
