class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[None]*(amount+1) for _ in range(n+1)]
        for j in range(amount+1):
            dp[0][j] = inf
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i][j-coins[i-1]]+1, dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount] if dp[n][amount]!=inf else -1