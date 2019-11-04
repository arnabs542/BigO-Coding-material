#Toeplitz matrix
def isToeplitzMatrix(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True

matrix = [[1,2],[2,2]]
print(isToeplitzMatrix(matrix))
