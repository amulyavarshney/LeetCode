# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def rec(node):
            if not node:
                return 0, True
            if node.left is None and node.right is None:
                return 1, True
            isBalanced = False
            L, isLeft = rec(node.left)
            R, isRight = rec(node.right)
            if not isLeft or not isRight:
                return max(L, R) + 1, False
            if L == R or L == R+1 or L+1 == R:
                isBalanced = True
            return max(L, R) + 1, isBalanced
        return rec(root)[1]