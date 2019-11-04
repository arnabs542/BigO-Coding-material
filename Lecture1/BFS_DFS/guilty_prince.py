#guilty prince: http://lightoj.com/volume_showproblem.php?problem=1012

import queue 

MAX = 405



class point:

    def __init__(self,x, y):
        self.x = x 
        self.y = y

def isValid(pt, maze):
    return pt.x >= 0 and pt.x < w and pt.y >= 0 and pt.y < h and maze[pt.y][pt.x] == '.'


def BFS(src):
    count = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False for xx in range(w)] for yy in range(h)]
    visited[src.y][src.x] = True 
    q = queue.Queue()
    q.put(src)

    while not q.empty():
        u = q.get()

        for k in range(len(dx)):
            v = point(u.x + dx[k],u.y + dy[k])
           
            if isValid(v, maze) and not visited[v.y][v.x]:
                visited[v.y][v.x] = True 
                q.put(v)
                count += 1

    #print(count)
    return count 


if __name__ == '__main__':
    testcase = int(input())
    for t in range(testcase):
        w, h = map(int,input().split())
        
        maze = []
        for i in range(h):
            maze.append(input())

        for i in range(h):
            for j in range(w):
                if maze[i][j] == '@':
                    start = point(j,i)
        
        print('start: ', start.x, start.y)
        for m in maze:
            print(m)
        
        
        result = BFS(start)
        print(f'Case {t+1}:', result)
        
    
   