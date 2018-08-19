class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ret = []
        for i in range(len(nums)):
            n = abs(nums[i]) - 1
            if nums[n] < 0:
                ret.append(n + 1)
            else:
                nums[n] *= -1
        
        return ret