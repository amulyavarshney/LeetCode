class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = s = prices[0]
        m = s-b
        for i in range(1, len(prices)):
            if b > prices[i]:
                b = s = prices[i]
            elif s < prices[i]:
                s = prices[i]
            m = max(m, s-b)
        return m