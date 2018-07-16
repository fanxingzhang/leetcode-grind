class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in d:
                return [d[diff], i]
            d[v] = i;    
        return 0