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


def topologicalSort(graph, result):
    visited = [False] * V
    state = [0] * V

    # for i in range(V):
    #     if visited[i] == False:
    #         dfs(i, graph, visited, result)

    for i in range(V):
        if state[i] == 0:
            flag = dfs_detect_cyle(i, graph, state, result)
            if flag == False:
                return False

    result.reverse()
    return True


if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for i in range(V)]
    result = []
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)

    dag = topologicalSort(graph, result)
    if dag == False:
        print('The graph is not DAG')
    else:
        print('Topological sort: ')
    # for i in range(V):
    #     print(result[i], end= ' ')
        print(result)
