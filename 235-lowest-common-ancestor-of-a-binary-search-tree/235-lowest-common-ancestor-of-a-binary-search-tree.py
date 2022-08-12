# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None: return None
        if root.val==p.val or root.val==q.val: return root
        left_tree = self.lowestCommonAncestor(root.left, p, q)
        right_tree = self.lowestCommonAncestor(root.right, p, q)
        if left_tree and right_tree:
            return root
        return left_tree or right_tree