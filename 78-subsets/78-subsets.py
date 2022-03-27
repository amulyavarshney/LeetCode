class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(i, x):
            if i==len(nums):
                ans.append(x)
                return
            rec(i+1, x+[nums[i]])
            rec(i+1, x)
        rec(0, [])
        return ans