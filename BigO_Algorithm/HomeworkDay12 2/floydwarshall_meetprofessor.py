#Meet professor
INF = int(1e9)

def FloydWarshall(graphA, graphB, distA, distB):
    for i in range(26):
        for j in range(26):
            if i == j:
                distA[i][j] = 0
                distB[i][j] = 0
            else:
                if graphA[i][j] != None and i != j:
                    distA[i][j] = graphA[i][j]
                if graphB[i][j] != None and i != j:
                    distB[i][j] = graphB[i][j]
    for k in range(26):
        for i in range(26):
            for j in range(26):
                #print(i,j,k)
                if distA[i][j] > distA[i][k] + distA[k][j]:
                    distA[i][j] = distA[i][k] + distA[k][j]
                if distB[i][j] > distB[i][k] + distB[k][j]:
                    distB[i][j] = distB[i][k] + distB[k][j]
                   
if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        graphA = [[None for i in range(26)] for j in range(26)]
        graphB = [[None for i in range(26)] for j in range(26)]
        distA = [[INF for i in range(26)] for j in range(26)]
        distB = [[INF for i in range(26)] for j in range(26)]
        for street in range(n):
            lst = list(input().split())
            if lst[0] == 'Y':
                if lst[1] == 'U':
                    graphA[ord(lst[2]) - 65][ord(lst[3]) - 65] = int(lst[4])
                else:
                    graphA[ord(lst[2])- 65][ord(lst[3])- 65] = int(lst[4])
                    graphA[ord(lst[3])- 65][ord(lst[2])- 65] = int(lst[4])
            else:
                if lst[1] == 'U':
                    graphB[ord(lst[2])- 65][ord(lst[3])- 65] = int(lst[4])
                else:
                    graphB[ord(lst[2])- 65][ord(lst[3])- 65] = int(lst[4])
                    graphB[ord(lst[3])- 65][ord(lst[2])- 65] = int(lst[4])

        srcA, srcB = input().split()
        FloydWarshall(graphA, graphB, distA, distB)
        res = []
        temp = 0
        min_value = INF
        pos_list = []
        for i in range(26):
            temp = distA[ord(srcA)-65][i] + distB[ord(srcB)-65][i]
            if temp < min_value:
                min_value = temp
                pos_list = []
                pos_list.append(chr(i+65))
            elif temp == min_value:
                pos_list.append(chr(i+65))

        if min_value < INF:
            print(min_value, ' '.join(pos_list))
        else:
            print('You will never meet.')
        
