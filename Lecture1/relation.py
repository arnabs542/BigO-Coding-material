#Answer the boss
#Example:
# Input:
# 5 6 #5 vertices and 6 edges 
# 2 0 #employee 2's rank is lower than employee 0'rank meaning 0 -> 2
# 2 4 # 4 -> 2 
# 1 4 # 4 -> 1
# 1 2 # 2 -> 1
# 3 2 # 2 -> 3
# 4 0 # 0 -> 4

# Output:
# 1 0
# 2 4 
# 3 2
# 4 1
# 4 3

#Output topo: 0 -> 4 -> 2 -> 1 -> 3

0 -> 1 -> 2
4 - 5 -> 3 -> 2

Output: 0 -> 1 -> 3 -> 2 or 0 -> 3 -> 1 -> 2 
#Rank: # of edges to the node in the graph


def dfs_detect_cycle(u, graph, state, result):
  # 0: not visited
  # 1: visited
  # 2: on path
  state[u] = 2
  # graph[u].sort(reverse=True)
  for v in graph[u]:
    if state[v] == 2:
      return False
    if state[v] == 0:
      if dfs_detect_cycle(v, graph, state, result) == False:
        return False

  state[u] = 1
  result.append(u)
  return True


def topologicalSort(graph, result):
    # visited = [False] * 26
    
    # for i in range(26):
    #     if visited[i] == False:
    #         dfs(i, graph, visited, result)

    # result.reverse()


  for i in range(26):
    if state[i] == 0:
      flag = dfs_detect_cycle(i, graph, state, result)
      if flag == False:
        print('Cycle detected')
        exit(0)


  result.reverse()

  return True


if __name__ == '__main__':
  testcase = int(input())
  for case in range(testcase):
