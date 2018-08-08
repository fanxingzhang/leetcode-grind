# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nh = ListNode(-1)
        nh.next = head
        curr = head
        prev = nh
        while curr and curr.next:
            if curr.val == curr.next.val:
                temp = curr.next
                while temp and temp.val == curr.val:
                    temp = temp.next
                curr = temp
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return nh.next