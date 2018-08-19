class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i > a:
                nums[i], nums[a] = nums[a], nums[i]
                a += 1
            elif nums[i] == 2 and i < b:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
            else:
                i += 1