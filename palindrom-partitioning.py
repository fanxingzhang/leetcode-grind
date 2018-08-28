class Solution(object):
    def __init__(self):
        self.d = {}
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        if s in self.d:
            return self.d[s]
        if len(s) == 1:
            return [[s]]

        temp = ""
        ret = []
        for i in range(len(s)):
            temp += s[i]
            if temp == temp[::-1]:
                temp2 = self.partition(s[i + 1:])
                if temp2:
                    ret += [[temp] + x for x in temp2]
                else:
                    ret += [[temp]]
        self.d[s] = ret
        return ret

                