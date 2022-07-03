class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        dp = [[0, 0] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1]+1)
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0]+1)
        return max(dp[-1])+1