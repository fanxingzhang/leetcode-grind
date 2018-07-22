class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        a = True
        while a and i >= 0:
            digits[i] += 1
            if digits[i] >= 10:
                digits [i] -= 10
                i -= 1
            else:
                a = False
        if a == True:
            digits.insert(0, 1)
        return digits
        
            