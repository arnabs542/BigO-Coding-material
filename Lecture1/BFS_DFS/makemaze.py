#MAKEMAZE: https://www.spoj.com/problems/MAKEMAZE/
import queue 

def printMaze(maze,x,y):
    for i in range(m):
        for j in range(n):
            if i == x and j == y:
                print('x',end = ' ')
            else:
                print(maze[i][j], end =' ')
        print()

    print('---------------------')

def isValid(point, maze):
    return point[0] >= 0 and point[0] < n and point[1] >= 0 and point[1] < m and maze[point[0]][point[1]] == '.' 


def BFS(start, end, maze):
    result = False 

    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    visited = [[False for xx in range(n)] for yy in range(m)]
    visited[start[0]][start[1]] = True 

    q = queue.Queue()
    q.put(start)
    printMaze(maze,start[0],start[1])

    while not q.empty():
        u = q.get()
        
        
        for k in range(len(dx)):
            vx = u[0] + dx[k] 
            vy = u[1] + dy[k]
            v = (vx, vy)
            if isValid(v, maze) and not visited[vx][vy]:
                visited[vx][vy] = True 
                printMaze(maze, vx, vy)
                if vx == end[0] and vy == end[1]: 
                    return True 
                q.put(v)

    return result 


if __name__ == '__main__':
    test_case = int(input())
    for _ in range(test_case):
        m, n = map(int,input().split())
        maze = []
        for i in range(m):
            maze.append(input())

        points = []
        for i in range(m):
            for j in range(n):
                if maze[i][j] == '.' and (j == 0 or j == n-1 or i == 0 or i == m-1):
                    points.append((i,j))

        if len(points) == 2:
            if BFS(points[0], points[1], maze):
                print('valid')
            else:
                print('invalid')
        else:
            print('invalid')