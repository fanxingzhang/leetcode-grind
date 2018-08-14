class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1
            
        for c in ransomNote:
            if d.get(c, 0) <= 0:
                return False
            d[c] = d[c] - 1
        
        return True
            