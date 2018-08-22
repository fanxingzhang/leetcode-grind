class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        for i in nums:
            d[i] += 1
        a = [-1] * len(nums)
        for i in d:
            if a[d[i] - 1] > 0:
                a[d[i] - 1].append(i)
            else:
                a[d[i] - 1] = [i]
        ret = []
        for i in a[::-1]:
            if i != -1:
                ret += i
        return ret[:k]
        