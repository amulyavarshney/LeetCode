class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9+7
        prev, cur = 1, 1
        for i in range(1, n):
            cur = (2*i*i+3*i+1)*prev
            prev = cur%mod
        return prev