# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        p3 = head
        c = 1
        while c < n:
            p1 = p1.next
            c += 1
        while p1.next:
            p3 = p2
            p1 = p1.next
            p2 = p2.next
        if p3 == head and p2 == head:
            return head.next
        p3.next = p2.next
        return head