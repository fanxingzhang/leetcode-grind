class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        a = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            a.append((matrix[i][0], i, 0))
        heapq.heapify(a)
        for i in range(k):
            temp = heapq.heappop(a)
            if temp[2] < m - 1:
                heapq.heappush(a, (matrix[temp[1]][temp[2] + 1], temp[1], temp[2] + 1))
        return temp[0]
        