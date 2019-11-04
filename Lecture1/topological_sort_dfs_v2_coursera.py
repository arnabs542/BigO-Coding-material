#Implement the topological ordering based on DFS inspired style
#Pseudocode:

# - Run DFS on each of the unvisited vertex
# - In each DFS, once encountered sink vertex or vertex whose neighbors have all been visited
# - Store the vertex into a result array and return to previous vertex


def dfs(u, graph, visited, result):
    visited[u] = True
    print('Node: ', u)
    for v in graph[u]:
        if visited[v] == False:
            dfs(v, graph, visited, result)

    result.append(u)
    print(result)


def dfs_detect_cyle(u, graph, state, result):
    state[u] = 2
    for v in graph[u]:
        if state[v] == 2:
            return False
        if state[v] == 0:
            if not dfs_detect_cyle(v, graph, state, result):
                return False



    state[u] = 1
    print('State: ', state)
    result.append(u)
    return True

def DFS(graph, visited, s):
    global current_label
    visited[s] = True
    for w in graph[s]:
        if visited[w] == False:
            DFS(graph, visited, w)

    result[s] = current_label
    current_label -= 1



def DFS_loop(graph):
    visited = [False] * V

    for i in range(V):
        if visited[i] == False:
            DFS(graph, visited, i)




if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for i in range(V)]
    result = [0 for i in range(V)]
    current_label = V 
    for i in range(E):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)

    DFS_loop(graph)
    print(result)
