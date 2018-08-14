class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        max = 0
        for i in range(len(nums)):
            if i > max:
                return False
            if i + nums[i] > max:
                max = i + nums[i]
        return max >= len(nums) - 1