class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = {}
        count = 0
        for j in J:
            dic[j] = 1
        for s in S:
            if s in dic:
                count += 1
        return count