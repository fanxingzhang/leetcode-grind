class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b, c = float('-inf'), float('-inf'), float('-inf')
        
        for i in range(0, len(nums)):
            if nums[i] > c:
                a = b
                b = c
                c = nums[i]
            elif nums[i] > b and nums[i]  < c:
                a = b
                b = nums[i]
            elif nums[i] > a and nums[i] < b:
                a = nums[i]
        return c if a == float('-inf') else a
                