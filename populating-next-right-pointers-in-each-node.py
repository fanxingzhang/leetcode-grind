# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        p = [[root]]
        while p:
            temp = p.pop(0)
            new = []
            for i in range(len(temp)):
                if i + 1 >= len(temp):
                    temp[i].next = None
                else:
                    temp[i].next = temp[i + 1]
                if temp[i].left:
                    new.append(temp[i].left)
                if temp[i].right:
                    new.append(temp[i].right)
            if new:
                p.append(new)
            