class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(A)):
            for j in range(len(B)):
                s = A[i] + B[j]
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1
        ret = 0
        for i in range(len(C)):
            for j in range(len(D)):
                s = C[i] + D[j]
                if -s in d:
                    ret += d[-s]
                    
        return ret