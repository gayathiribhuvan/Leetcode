class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        zeros = []
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        for i,j in zeros:
            for x in range(0,r):
                matrix[x][j] = 0
            for y in range(0,c):
                matrix[i][y] = 0
