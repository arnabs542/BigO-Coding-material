#Input example:
"""
Input:
4 2
1 3
2 3 4
Graph: 1 --> 3 / 2 --> 3 and 2 --> 4

Output: 4 0 1 2
4 --> 1
2: mainboss 
1 --> 3
2 --> 4 
"""
def dfs(src):
	visited[src] = True
	for u in graph[src]:
		if not visited[u]:
			dfs(u)

	result.append(src+1)


def topological_sort_dfs(graph, result):
	for v in range(N):
		if not visited[v]:
			dfs(v)

	result.reverse()


#input: 2 --> 4 --> 1 --> 3
#output: 4 0 1 2 
def boss(arr):
	boss_arr = [0] * N
	for i in range(1, N):
		boss_arr[result[i]-1] = result[i-1]

	return boss_arr

if __name__ == '__main__':
	N, K = map(int, input().split())
	graph = [[] for i in range(N)]
	visited = [False] * N
	result = []
	for i in range(K):
		ls = list(map(int, input().split()))
		w = ls[0]
		for e in range(w):
			graph[i].append(ls[e+1] - 1)


	topological_sort_dfs(graph, result)
	#print(boss(result))

	boss_result = boss(result)
	for res in boss_result:
		print(res)

