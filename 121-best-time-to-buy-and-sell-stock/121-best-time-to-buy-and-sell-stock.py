class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                ans = max(ans, prices[i]-buy)
        return ans