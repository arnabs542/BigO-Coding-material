def topology_sort():
	for v in range(N):
		if not visited[v]:
			print('Topo: ', v)
			dfs(v)

	return result.reverse()


def dfs(vertex):
	visited[vertex] = True 
	print('DFS: ', vertex)
	for node in graph[vertex]:
		if not visited[node]:
			dfs(node)

	result.append(vertex)
	print('Interim result: ', result)	

if __name__ == '__main__':
	N, E = map(int, input().split())
	graph = [[] for i in range(N)]
	visited = [False] * N
	result = []
	for i in range(E):
		u, v = map(int,input().split())
		graph[u].append(v)

	for node in graph:
		print(node)

	topology_sort()	
	print(result)

