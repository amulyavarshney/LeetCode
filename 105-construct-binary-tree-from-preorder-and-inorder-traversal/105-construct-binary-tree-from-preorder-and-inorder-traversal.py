# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildSubtree(left, right):
            if left>right:
                return None
            nonlocal preInd
            node = TreeNode(preorder[preInd])
            preInd += 1
            node.left = buildSubtree(left, d[node.val]-1)
            node.right = buildSubtree(d[node.val]+1, right)
            return node
        d = {}
        for i,x in enumerate(inorder):
            d[x] = i
        preInd = 0
        return buildSubtree(0, len(preorder)-1)