class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[-1]*(n+1) for _ in range(m+1)] for __ in range(len(strs))]
        def rec(i, m, n):
            if(i<0):
                return 0
            if dp[i][m][n] != -1:
                return dp[i][m][n]
            zeros = strs[i].count('0')
            ones = len(strs[i])-zeros
            if(zeros > m or ones > n):
                dp[i][m][n] = rec(i-1, m, n)
            else:
                dp[i][m][n] = max(rec(i-1, m-zeros, n-ones)+1, rec(i-1, m, n))
            return dp[i][m][n]
        return rec(len(strs)-1, m, n)