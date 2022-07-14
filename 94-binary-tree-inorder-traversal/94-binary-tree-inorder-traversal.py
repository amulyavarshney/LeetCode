# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
            else:
                break
        return ans