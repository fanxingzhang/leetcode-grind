class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        a = [1] * len(nums)
        ret = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    a[i] = max(a[i], a[j] + 1)
            ret = max(ret, a[i])
        return ret