# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(i, j):
            if i > j: 
                return
            mid = i + (j-i)//2
            root = TreeNode(nums[mid])
            root.left = solve(i, mid-1)
            root.right = solve(mid+1, j)
            return root
        return solve(0, len(nums)-1)