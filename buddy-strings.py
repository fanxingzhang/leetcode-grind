class Solution(object):
    def buddyStrings(self, a, b):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(a) != len(b):
            return False
        
        if a == b and len(a) != len(set(a)):
            return True
        
        c = [[a[i], b[i]] for i in range(len(a)) if a[i] != b[i]]
        return len(c) == 2 and c[0][0] == c[1][1] and c[0][1] == c[1][0]