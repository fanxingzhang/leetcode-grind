# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        ret = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i].start <= ret[-1].end:
                ret[-1].end = max(ret[-1].end, intervals[i].end)
            else:
                ret.append(intervals[i])
    
        return ret