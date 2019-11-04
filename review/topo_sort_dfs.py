
def dfs_v2(src): # with cycle detecting capability
	
	state[src] = 2

	for u in graph[src]:

		if state[u] == 2:
			print('Cycle detected at: ', u)
			exit(1)

		if state[u] == 0:
			dfs_v2(u)


	state[src] = 1
	result.append(src)
	print('Intermediate result: ', result)



de dfs_v1(src): # without cycle detecting capability
	visited[src] = True

	for u in graph[src]:
		if not visited[u]:
			dfs_v1(u)

	result.append(src)
	print('Intermediate result: ', result)


def topological_sort_dfs_v1(graph, result):
	
	for v in range(V):
		print('Examined Node: ', v)
		if not visited[v]:
			dfs_v1(v)

	
	result.reverse()
	
	return result


def topological_sort_dfs_v2(graph, result):
	
	for v in range(V):
		print('Examined Node: ', v)
		if state[v] == 0:
			dfs_v2(v)

	
	result.reverse()
	
	return result


if __name__ == '__main__':
	V, E = map(int, input().split())
	graph = [[] for i in range(V)]
	visited = [False] * V
	
	# state array to keep track of 3 states: 
	#{'0': unvisited, '1': visited, '2': visited but not finish visiting neighboring nodes}
	state = [0] * V
	
	result = []

	for i in range(E):
		u, v = map(int, input().split())
		graph[u].append(v)

	
	#for v in graph:
	#	print(v)

	
	#topological_sort_dfs_v1(graph, result)
	topological_sort_dfs_v2(graph, result)
	print('Final result: ', result)
