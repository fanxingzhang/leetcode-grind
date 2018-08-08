# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}
        def helper(n, l):
            if not n:
                return l
            if l not in d:
                d[l] = []
            d[l].append(n.val)
            a = helper(n.left, l + 1)
            b = helper(n.right, l + 1)
            return max(a,b)
        depth = helper(root, 0)
        r = []
        for i in range(depth - 1, -1, -1):
            r.append(d[i])
        return r