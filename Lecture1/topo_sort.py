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



if __name__ == '__main__':
  V, E = map(int, input().split())
  graph = [[] for i in range(V+1)]
  result = []
  for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)

  if (topologicalSort(graph, result)):
    # print('Topological Sort of graph: ')
    for i in range(V):
      print(result[i], end = ' ')
  else:
    print('Sandro fails')
