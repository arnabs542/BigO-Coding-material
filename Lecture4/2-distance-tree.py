import queue 


def bfs(src, graph, visited, k, pairs):
	depth_limit = k
	q = queue.Queue()
	q.put(src)
	visited = [False for i in range(n)]
	visited[src] = True
	dist = [0 for i in range(n)]
	dist[src] = 0
	#print(src)
	while not q.empty():
		#print(q.queue)
		v = q.get()	
		for w in graph[v]:
			if not visited[w]:
				visited[w] = True
				dist[w] = dist[v] + 1
				if dist[w] <= k:
					q.put(w)
					if dist[w] == k:	
						if src < w:
							a, b = src, w
						else:
							a, b = w, src	
						pairs.add((a + 1,b + 1))

	
	


def find_k_distance(graph, visited, n, k):
	pairs = set() 
	for i in range(n):
		bfs(i, graph, visited, k, pairs)

	return pairs


if __name__ == '__main__':
	n,k = map(int, input().split())
	graph = [[] for i in range(n)]
	visited = [False for i in range(n)]
	path = [-1 for i in range(n)]
	for i in range(n-1):
		u, v = map(int, input().split())
		graph[u-1].append(v-1)
		graph[v-1].append(u-1)

	pairs = find_k_distance(graph, visited, n, k)
	print(len(pairs))
