class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        t = [0]*(n+1)
        for i in range(1, n+1):
            t[i] = max(t[i-2]+nums[i-1], t[i-1])
        return t[n]