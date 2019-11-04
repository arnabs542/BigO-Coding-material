import queue 


def topology_kahn_sort():
	for v in range(N):
		if indegree[v] == 0:
			zero_indegree.put(v)

	while not zero_indegree.empty(): 
		u = zero_indegree.get()
		print('Node: ', u)
		result.append(u)
		for neighbor in graph[u]:
			indegree[neighbor] -= 1
			if indegree[neighbor] == 0:
				zero_indegree.put(neighbor)
		print('Interim result: ', result)
			


if __name__ == '__main__':
	N, E = map(int, input().split())
	graph = [[] for i in range(N)]
	visited = [False] * N
	indegree = [0] * N 
	#zero_indegree = []
	zero_indegree = queue.Queue()
	result = []
	for i in range(E):
		u, v = map(int,input().split())
		graph[u].append(v)
		indegree[v] += 1

	topology_kahn_sort()	
	print(result)

