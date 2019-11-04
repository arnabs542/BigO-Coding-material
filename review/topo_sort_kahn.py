import queue 


def topological_sort_kahn(graph, indegree, zero_indegree, result):
	
	while not zero_indegree.empty():
		print('Intermediate zero_indegree: ', zero_indegree.queue)
		s = zero_indegree.get()
		print('Node added: ', s)
		result.append(s)
		for u in graph[s]:
			indegree[u] -= 1
			if indegree[u] == 0:
				zero_indegree.put(u)

	for i in range(V):
		if indegree[i] != 0:
			print('Cycle detected!')
			exit(1)
	


if __name__ == '__main__':
	V, E = map(int, input().split())
	graph = [[] for i in range(V)]
	indegree = [0] * V
	#zero_indegree = []
	zero_indegree = queue.Queue()
	result = []
	for i in range(E):
		u, v = map(int, input().split())
		graph[u].append(v)
		indegree[v] += 1

	print('Original indegree: ', indegree)	
	for i in range(V):
		if indegree[i] == 0:
			zero_indegree.put(i)
	
	topological_sort_kahn(graph, indegree, zero_indegree, result)
	
	print(result)
