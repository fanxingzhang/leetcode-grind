# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        odd = head
        eh = head.next
        even = head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next 
            odd = odd.next
            even = even.next
        odd.next = eh
        return head