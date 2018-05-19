class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for a in A:
            for index in range(0, len(a)/2):
                temp = a[index]
                a[index] = a[len(a) - 1 - index]
                a[len(a) - 1 - index] = temp
            for i in range(0, len(a)):
                a[i] = (0 if a[i] == 1 else 1)
        return A