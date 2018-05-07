class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c : i for i, c in enumerate(S)}
        
        ans = []
        currMax = 0
        lastMax = -1
        for i, c in enumerate(S):
            if i > currMax:
                ans.append(currMax - lastMax)
                lastMax = currMax
            currMax = max(last[c], currMax)
            
        ans.append(currMax - lastMax)
        return ans
        