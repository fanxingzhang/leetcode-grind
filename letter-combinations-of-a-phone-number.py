class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        mapping = [ None,
            None,
            ["a","b","c"],
            ["d","e","f"],
            ["g","h","i"],
            ["j","k","l"],
            ["m","n","o"],
            ["p","q","r","s"],
            ["t","u","v"],
            ["w","x","y","z"]]

        def helper(s):
            if len(s) == 1:
                return mapping[int(s)]
            c = s[0]
            ret = []
            for l in mapping[int(c)]:
                ret += [l + x for x in helper(s[1:])]
            return ret
        return helper(digits)
            