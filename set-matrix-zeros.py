class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        c = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        c = 0
                    else:
                        matrix[0][j] = 0
                            
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0
                    
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0
        if c == 0:
            for j in range(0, len(matrix)):
                matrix[j][0] = 0
        