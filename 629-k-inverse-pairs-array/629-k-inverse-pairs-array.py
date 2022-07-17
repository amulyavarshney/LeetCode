class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9+7
        dp = [[-1]*(k+1) for _ in range(n+1)]
        def rec(n, k):
            if n==0:
                return 0
            if k==0:
                return 1
            if dp[n][k] != -1:
                return dp[n][k]
            x = rec(n-1, k-n) if (k-n)>=0 else 0
            ans = (rec(n-1, k)+mod-x)%mod
            # for i in range(min(k+1, n)):
            #     ans = (ans + rec(n-1, k-i))%mod
            dp[n][k] = (rec(n, k-1)+ans)%mod
            return dp[n][k]
        return (rec(n, k)+mod-(rec(n, k-1) if k>0 else 0))%mod