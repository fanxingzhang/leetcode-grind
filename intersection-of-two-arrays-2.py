class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        ret = []
        for n in nums1:
            d[n] += 1
        for n in nums2:
            if d[n] > 0:
                ret.append(n) 
                d[n] -= 1
        return ret