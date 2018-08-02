class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ret = [[]]
        for i in nums:
            for j in ret[:len(ret)]:
                ret.append(j + [i]])
        return ret