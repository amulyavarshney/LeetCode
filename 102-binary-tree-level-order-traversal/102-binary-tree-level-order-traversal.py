# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([(root, 0)])
        res = []
        while queue:
            node, level = queue.popleft()
            if len(res) > level:
                res[level].append(node.val)
            else:
                res.append([node.val])
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        return res