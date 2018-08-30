class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        if k > l:
            k = k % l
        for i in range(l / 2):
            nums[i], nums[l - 1 - i] = nums[l - 1 - i], nums[i]
        for i in range(k/2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        for i in range(k, k + ((l - k) / 2)):
            nums[i], nums[l + k - 1 - i] = nums[l + k - 1 - i], nums[i]