#Fox and Names
# Input:
# 3
# rivest
# shamir
# adleman

# meaning: rivest < shamir < adleman 

# Output:
# bcdefghijklmnopq rsa tuvwxyz

# Input2:
# 10 
# petr 
# egor 
# endagorion 
# feferivan 
# ilovetanyaromanova 
# kostka 
# dmitriyh 
# maratsnowbear 
# bredorjaguarturnik 
# cgyforever

# Output2:
# aghjlnopefikdmbcqrstuvwxyz

# Pseudocode:
# - Build graph of characters by: comparing pair of names 
# if names[i][j] < names[i+1][j] => names[i][j] -> names[i+1][j]

# topologicalSort to get the order and fill in remaining characters

def dfs(u, graph, visited, result):
    visited[u] = True
    # print('Node: ', u)
    for v in graph[u]:
        if visited[v] == False:
            dfs(v, graph, visited, result)

    result.append(u)
    # print(result)



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
        print('Impossible')
        exit(0)


  result.reverse()

  return True




def compareNames(s, t):
  #Given that s < t
  #find the s[i] < t[i]
  
  

  string_len = min(len(s), len(t))
  for i in range(string_len):
    if s[i] != t[i]:
      return [s[i], t[i]]
      
  if len(t) < len(s):
    print('Impossible')
    print(t)
    print(s)
    exit(0)

  return None


if __name__ == '__main__':
  n = int(input())
  name_ls = []
  graph = [[] for i in range(26)]
  result = []
  state = [0 for i in range(26)]
  #Get input names in order 
  for i in range(n):
    name_ls.append(input())
  
  #Process the name list to generate characters order 
  for i in range(n-1):
    order_ls = compareNames(name_ls[i], name_ls[i+1])
    # print(order_ls[0])
    # print(order_ls)
    if order_ls:
      
      graph[ord(order_ls[0])-97].append(ord(order_ls[1])-97) 

  # print(graph)
  topologicalSort(graph, result)
  for res in result:
    print(chr(res + 97), end = '')
  print()

