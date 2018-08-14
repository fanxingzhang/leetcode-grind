class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        
        if len(start) != len(end):
            return False
        
        a = []
        b = []
        
        for i in range(len(start)):
            if start[i] != end[i]:
                if start[i] == "R" and end[i] == "X":
                    a.append(1)
                elif start[i] == "X" and end[i] == "R":
                    if not a:
                        return False
                    a.pop()

                elif start[i] == "X" and end[i] == "L":
                    b.append(1)
                elif start[i] == "L" and end[i] == "X":
                    if not b:
                        return False
                    b.pop()
                else:
                    return False
                
        return not a and not b