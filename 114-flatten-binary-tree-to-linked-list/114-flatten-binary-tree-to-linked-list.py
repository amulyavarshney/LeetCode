# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        def rec(node):
            if not node:
                return node
            temp = node.right
            node.right = rec(node.left)
            node.left = None
            rnode = node
            while rnode.right:
                rnode = rnode.right
            rnode.right = temp
            rec(node.right)
            return node
        rec(root)