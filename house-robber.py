class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        a = range(len(nums))
        a[0], a[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a[i] = max(a[i - 1], a[i - 2] + nums[i])
        return a[-1]