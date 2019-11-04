import queue 


def topology_kahn_sort():
	for v in range(n):
		if indegree[v] == 0:
			zero_indegree.put(v)

	#print(zero_indegree.queue)
	while not zero_indegree.empty(): 
		u = zero_indegree.get()
		#print('Node: ', u+1)
		result.append(u+1)
		for neighbor in graph[u]:
			indegree[neighbor] -= 1
			if indegree[neighbor] == 0:
				zero_indegree.put(neighbor)
		#print('Interim result: ', result)
	
	if sum(indegree) != 0:
		result.clear()

if __name__ == '__main__':
	n, m = map(int, input().split())
	graph = [[] for i in range(n)]
	visited = [False] * n
	zero_indegree = queue.PriorityQueue()
	indegree = [0] * n 
	result = [] 
	for i in range(m):
		u, v = map(int,input().split())
		graph[u-1].append(v-1)
		indegree[v-1] += 1


	topology_kahn_sort()	
	if result:
		print(result)
	else:
		print('Sandro fails.')

