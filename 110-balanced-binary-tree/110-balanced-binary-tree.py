# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def height(root):
            nonlocal flag
            if not root:
                return 0
            left, right = 0, 0
            if root.left:
                left = height(root.left)
            if root.right:
                right = height(root.right)
            if abs(left-right)>1:
                flag = False
            return max(left, right)+1
        _ = height(root)
        return flag