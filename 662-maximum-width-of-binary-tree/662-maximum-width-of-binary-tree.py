# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([(root,1,1)])
        start, pl, prev = 1, 1, 1
        ans = 1
        while len(queue)>0:
            node, l, idx = queue.popleft()
            if l!=pl:
                ans = max(ans, prev-start+1)
                start, pl = idx, l
            if node.left:
                queue.append((node.left,l+1,2*idx))
            if node.right:
                queue.append((node.right,l+1,2*idx+1))
            prev = idx
        return max(ans, prev-start+1)