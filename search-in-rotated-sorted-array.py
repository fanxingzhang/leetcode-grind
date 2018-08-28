class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        def helper(l, r, t):
            if l == r:
                if t == nums[l]:
                    return l
                else:
                    return -1
            
            m = l + ((r - l) / 2)
            if nums[m] == t:
                return m
            if t < nums[m]:
                if t < nums[l] and nums[r] < nums[m]:
                    return helper(m + 1, r, t)
                else:
                    return helper(l, m, t)
            else:
                if t > nums[r] and nums[l] > nums[m]:
                    return helper(l, m, t)
                else:
                    return helper(m + 1, r, t)
                
        return helper(0, len(nums) - 1, target)