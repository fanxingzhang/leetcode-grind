# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a  = headA
        b = headB
        l = 0
        while a:
            a = a.next
            l += 1
        l2 = 0
        while b:
            b = b.next
            l2 += 1
        a  = headA
        b = headB
        if l > l2:
            for i in range(l - l2):
                a = a.next
        else:
            for i in range(l2 - l):
                b = b.next
        while a != b:
            a, b = a.next, b.next
        return a