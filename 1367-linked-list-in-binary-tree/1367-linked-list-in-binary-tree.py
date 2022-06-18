# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(root):
            def dfs_inner(node, curr):
                if not curr:
                    return True
                if not node:
                    return False
                return node.val == curr.val and (dfs_inner(node.left, curr.next) or dfs_inner(node.right, curr.next))
            if not head:
                return True
            if not root:
                return False
            return dfs_inner(root, head) or dfs(root.left) or dfs(root.right)
        return dfs(root)
        