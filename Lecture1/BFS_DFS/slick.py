#Slick: https://www.spoj.com/problems/UCV2013H/
import queue 

MAX = 250*250 

class node:

    def __init__(self, r, l):
        self.r = r
        self.l = l


def isValid(point):
    # print(point.r >=0, point.r < row, point.l>=0,point.l < col,maze[point.r][point.l])
    return point.r >= 0 and point.r < row and point.l >= 0 and point.l < col and maze[point.r][point.l] == '1'


def BFS(point):
    dr = [1,0,-1,0]
    dl = [0,-1,0,1]
    q = queue.Queue()
    q.put(point)
    visited[point.r][point.l] = True

    temp_slick_size = 1
    while not q.empty():
        u = q.get()
        for k in range(len(dr)):
            v = node(u.r + dr[k], u.l + dl[k]) 
            if isValid(v) and not visited[v.r][v.l]:
                visited[v.r][v.l] = True 
                q.put(v)
                temp_slick_size += 1 

            
    return temp_slick_size
                


if __name__ == '__main__':
    while True:
        row, col = map(int,input().split())
        if row == 0 and col == 0:
            break 
        maze = []
        for i in range(row):
            maze.append(input())
        visited = [[False for xx in range(col)] for yy in range(row)]        
       
        for i in range(row):
            for j in range(col):
                print(maze[i][j],end=' ')
            print()

        count = 0
        for i in range(row):
            for j in range(col):
                if maze[i][j] == '1' and visited[i][j] == False:
                    vertex = node(i,j)
                    print('start node: ', vertex.r, vertex.l)
                    print('size: ', BFS(vertex)) 
                    count += 1
        
        print('Count: ',count)