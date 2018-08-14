class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        ret = []
        
        for i in range(numRows):
            if i == 0:
                ret.append([1])
            elif i == 1:
                ret.append([1, 1])
            else:
                temp = [ret[-1][j - 1] + ret[-1][j] for j in range(1, len(ret[-1]))]
                temp.insert(0, 1)
                temp.append(1)
                ret.append(temp)
        
        return ret