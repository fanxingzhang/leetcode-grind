class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for a in matrix:
            for index in range(0, len(a)/2):
                temp = a[index]
                a[index] = a[len(a) - 1 - index]
                a[len(a) - 1 - index] = temp