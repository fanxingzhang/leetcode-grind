class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums) - 1)
        

    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        m = (l + r) / 2
        return max(self.helper(nums, l, m),
                  self.helper(nums, m + 1, r),
                  self.crossing(nums, l, m, r))
    
    def crossing(self, nums, l, m, r):
        s = nums[m]; ls = nums[m]
        for i in range(m - 1, l - 1, -1):
            s += nums[i]
            if s > ls: 
                ls = s
        s = nums[m + 1]; rs = nums[m + 1]
        for i in range(m + 2, r + 1):
            s += nums[i]
            if s > rs: 
                rs = s
        return rs + ls
            