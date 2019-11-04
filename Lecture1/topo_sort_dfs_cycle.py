from queue import PriorityQueue


def topologicalSort(graph, result):
  indegree = [0] * (V+1)
  zero_indegree = PriorityQueue()
  # zero_indegree = []
  for u in range(1,V+1):
    for v in graph[u]:
      indegree[v] += 1

  for i in range(1,V+1):
    if indegree[i] == 0:
      zero_indegree.put(i) #from smallest to largest vertex


  # total: O(Nlogn + M)
  while not zero_indegree.empty(): # O(n)
    # zero_indegree.sort()  #O(nlogn)
    # print(zero_indegree)
    u = zero_indegree.get() #O(logn)
    result.append(u)
    for v in graph[u]: #O(M)
      indegree[v] -= 1
      if indegree[v] == 0:
        zero_indegree.put(v)





  for i in range(1,V+1):
    if indegree[i] != 0:
      # print(i)
      return False

  return True

# 1 -> 4
# 0 -> 2 -> 3 -> 1

def dfs(u, graph, visited, result):
  visited[u] = True
  for v in graph[u]:
    if not visited[v]:
      dfs(v, graph, visited, result)

  result.append(u+1)


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
  result.append(u+1)
  return True


def topologicalSort_dfs(graph, state, result):

  for i in range(V):
    if state[i] == 0:
      flag = dfs_detect_cycle(i, graph, state, result)
      if flag == False:
        return False


  result.reverse()

  return True



if __name__ == '__main__':
  V, E = map(int, input().split())
  graph = [[] for i in range(V)]
  result = []
  state = [0 for i in range(V)]
  for i in range(E):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)


  if topologicalSort_dfs(graph, state, result):
    for i in range(V):
      print(result[i], end=' ')
  else:
    print('Sandro fails.')

  # if (topologicalSort(graph, result)):
  #   # print('Topological Sort of graph: ')
  #   for i in range(V):
  #     print(result[i], end = ' ')
  # else:
  #   print('Sandro fails.')
