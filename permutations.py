class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        def helper(a):
            if len(a) == 1:
                return [a]
            b = []
            for i in range(len(a)):
                c = helper(a[:i] + a[i + 1:])
                b += [[a[i]] + x for x in c]
            return b
            
        
        ret = helper(nums)
        return ret
        