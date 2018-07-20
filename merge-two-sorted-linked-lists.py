# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l2:
            return l1
        if not l1:
            return l2
        
        ret = ListNode(0)
        head = ret
        while l1 and l2:
            if l1.val < l2.val:
                c = l1.val
                l1 = l1.next
            else:
                c = l2.val
                l2 = l2.next
            ret.next = ListNode(c)
            ret = ret.next
        
        ret.next = l1 if l1 else l2

        return head.next
        
        
        
