#Implementation of DFS:

MAX = 100 
V = None 
E = None 
visited = [False]*MAX #Initialize explored territory as empty 
path = [0]*MAX #Initialize path 
graph = [[] for i in range(MAX)] #Initialize graph as 2D arrays 


#Depth First Search implementation
def DFS(src):
	for i in range(V):
		visited[i] = False 
		path[i] = -1 
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
	for v in graph[src]:
		if visited[v] == False:
			DFS_recursive(v)
			path[v] = src
		


#find the path from s to f
def printPath(s,f,path):
    b = []
    if f == s:
        print(f)
        return 

    if path[f] == -1:
        print('No path')
        return 
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break 
    for i in range(len(b)-1,-1,-1):
        print(b[i], end=' ')


if __name__ == '__main__':
	V, E = map(int,input().split())
	print('Input edges:')
	for i in range(E):
		u, v = map(int,input().split())
		graph[u].append(v)
		graph[v].append(u)

	s = 1
	d = 5 
	print('DFS from {0} to {1}'.format(s,d))
	DFS(s)
	printPath(s,d,path)
	print('Recursive version: ')
	for i in range(V):
		visited[i] = False 
		path[i] = -1 
	DFS_recursive(s)
	printPath(s,d,path)
	print()
