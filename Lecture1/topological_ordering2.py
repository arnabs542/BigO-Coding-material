#Implement topological ordering using DFS

MAX = 1000
V = None 
E = None 
visited = [False]*MAX #Initialize explored territory as empty 
path = [0]*MAX #Initialize path 
graph = [[] for i in range(MAX)] #Initialize graph as 2D arrays 
result = [] 
indegree = [0] * MAX
zero_indegree = []



def Kahn():
	while len(zero_indegree) != 0:
		u = zero_indegree.pop()
		result.append(u)
		for v in graph[u]:
			indegree[v] -= 1


if __name__ == '__main__':
	V, E = map(int,input().split())
	print('Input edges:')
	for i in range(E):
		u, v = map(int,input().split())
		graph[u].append(v)
		indegree[v] += 1


	for i in range(V):
		#print(i, graph[i])
		#print(i, indegree[i])
		if indegree[i] == 0:
			zero_indegree.append(i)

	print(zero_indegree)
	exit(1)
	for i in range(V):
		visited[i]	= False
	
	
