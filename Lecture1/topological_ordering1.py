#Implement topological ordering using DFS

MAX = 1000
V = None 
E = None 
visited = [False]*MAX #Initialize explored territory as empty 
path = [0]*MAX #Initialize path 
graph = [[] for i in range(MAX)] #Initialize graph as 2D arrays 
result = [] 

#Depth First Search implementation
def DFS(src):
	#for i in range(V):
	#	visited[i] = False 
	#	path[i] = -1 
	s = []
	visited[src] = True 
	s.append(src)


	while len(s) != 0:
		print('Stack: ', s)
		v = s.pop() 
		print('Current node: ', v)
		for w in graph[v]:
			if visited[w] == False:
				visited[w] = True 
				s.append(w)
				path[w] = v 
		


#DFS resursive implementation
def DFS_recursive(src):
	
	visited[src] = True
	print('Current node: ', src)
	for v in graph[src]:
		if visited[v] == False:
			DFS_recursive(v)
	
	result.append(src)



if __name__ == '__main__':
	V, E = map(int,input().split())
	print('Input edges:')
	for i in range(E):
		u, v = map(int,input().split())
		graph[u].append(v)

	
	for i in range(V):
		visited[i]	= False
	
	for i in range(V):
		if not visited[i]:
			DFS_recursive(i)

	for element in result:
		print(element, end=' ')
	print()
