class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                l.append(c)
            else:
                if len(l) == 0:
                    return False
                c2 = l.pop()
                if c == ')' and c2 != '(':
                    return False
                if c == ']' and c2 != '[':
                    return False
                if c == '}' and c2 != '{':
                    return False
        return len(l) == 0