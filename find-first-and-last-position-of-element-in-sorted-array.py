class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        l = len(nums)
        if l == 1: 
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        
        a = self.searchRange(nums[:l/2], target)
        b = self.searchRange(nums[l/2:], target)
        if a != [-1, -1] and b != [-1, -1]:
            return [a[0], l/2 + b[1]]
        elif a == [-1, -1] and b == [-1, -1]:
            return [-1, -1]
        elif b == [-1, -1]:
            return a
        else:
            return [l/2 + b[0], l/2 + b[1]]
            