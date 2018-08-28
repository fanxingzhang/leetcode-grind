class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        a = b = ret = nums[0]
        for n in nums[1:]:
            if n < 0:
                a, b = b, a
            a = max(a * n, n)
            b = min(b * n, n)
            ret = max(a, ret)
            
        return ret