class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def rec(s, i):
            if len(s)==k:
                ans.append(s[:])
                return
            for j in range(i, n):
                s.append(nums[j])
                rec(s, j+1)
                s.pop()
        for k in range(n+1):
            rec([], 0)
        return ans