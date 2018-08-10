# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = [[root]]
        ret = []
        while q:
            nodes = q.pop(0)
            temp = []
            new = []
            for n in nodes:
                if n:
                    temp.append(n.val)
                    if n.left:
                        new.append(n.left)
                    if n.right:
                        new.append(n.right)
            if temp:
                ret.append(temp)
            if new:
                q.append(new)
        return ret