from queue import PriorityQueue

def dfs(src):

  visited[src] = True

  for u in graph[src]:
    if not visited[u]:
      dfs(u)

  result.append(beverages_ls[src])
  # print('Intermediate result: ', result)



def topological_sort(graph, result):
  for i in range(n):
    if not visited[i]:
      dfs(i)

  result.reverse()

  # print('done: ', result)

def topological_sort_kahn(graph, result):
  indegree = [0]*n
  zero_indegree = PriorityQueue()
  for u in range(n):
    for v in graph[u]:
      indegree[v] += 1

  for i in range(n):
    if indegree[i] == 0:
      zero_indegree.put(i)

  while not zero_indegree.empty():
    u = zero_indegree.get()
    result.append(beverages_ls[u])
    for v in graph[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        zero_indegree.put(v)



if __name__ == '__main__':

  case = 0

  while True:
    try:
      n = int(input())
      case += 1
      beverages_ls = []
      graph = [[] for i in range(n)]
      visited = [False] * n
      result = []
      for i in range(n):
        beverages_ls.append(input())


      m = int(input())
      for e in range(m):
        temp_ls = list(input().split())
        bev1 = beverages_ls.index(temp_ls[0])
        bev2 = beverages_ls.index(temp_ls[1])
        graph[bev1].append(bev2)

        # print('Case {0}: {1}'.format(case, graph))

      topological_sort_kahn(graph, result)

      print('Case #{0}: Dilbert should drink beverages in this order:'.format(case), end=' ')
      # for res in result:
      #   print(res, end=' ')

      print(*result, end = '')
      print('.')
      print()
      temp = input()
    except EOFError as e:
      # print(e)
      break
