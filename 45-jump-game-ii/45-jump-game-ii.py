class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf]*n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(nums[i]+1):
                dp[i] = min(dp[i], 1+dp[min(i+j, n-1)])
        return dp[0]