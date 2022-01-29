class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, n = 0, len(prices)
        m = 0
        for j in range(1, n):
            if prices[j] < prices[j-1]:
                m += prices[j-1]-prices[i]
                i = j
        return m + prices[-1] - prices[i]