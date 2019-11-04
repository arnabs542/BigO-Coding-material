#Hierarchy problem
#Input:
# 4 2
# 1 3  #student 1 wants to be 3'boss
# 2 3 4 # student 2 wants to be 3 and 4's boss
# Ouput:
# 4
# 0
# 1
# 2

# graph: 2 -> 4 -> 1 -> 3


#Implement the topological ordering based on DFS inspired style
#Pseudocode:

# - Run DFS on each of the unvisited vertex
# - In each DFS, once encountered sink vertex or vertex whose neighbors have all been visited
# - Store the vertex into a result array and return to previous vertex


def dfs(u, graph, visited, result):
    visited[u] = True
    # print('Node: ', u)
    for v in graph[u]:
        if visited[v] == False:
            dfs(v, graph, visited, result)

    result.append(u)
    # print(result)





def topologicalSort(graph, result):
    visited = [False] * N
    

    for i in range(N):
        if visited[i] == False:
            dfs(i, graph, visited, result)

    

    result.reverse()
    
#5 -> 4 -> 1 -> 3 -> 7 -> 2 -> 6
#4 7 1 5 0 2 3
def boss(result):
  for i in range(N):
    result[i] += 1
  
  boss = [0] * N
  for i in range(1,N):
    boss[result[i]-1] = result[i-1]

  print(boss) 
  
  # print(result)
  # for i in range(N):
  #   pos_i = result.index(i + 1)
  #   if pos_i == 0:
  #     print(0)
  #   else:
  #     print(result[pos_i-1])



if __name__ == '__main__':
    N, K = map(int, input().split())
  
    graph = [[] for i in range(N)]
    result = []
    for i in range(K):
        # u, v = map(int, input().split())
        input_ls = list(map(int, input().split()))
        for wish in range(1, input_ls[0]+1):
          graph[i].append(input_ls[wish]-1)
    
    # print(graph)
    topologicalSort(graph, result)
    boss(result)



    
