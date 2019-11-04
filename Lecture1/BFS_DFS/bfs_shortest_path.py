import queue 



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
            print('valid maze')
        else:
            print('Invalid maze')