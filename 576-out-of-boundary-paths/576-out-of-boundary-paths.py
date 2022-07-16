class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9+7
        dirn = ((0,1), (1,0), (0,-1), (-1,0))
        dp = [[[-1]*(n) for _ in range(m)] for __ in range(maxMove+1)]
        def rec(move, x, y):
            if not(0<=x<m and 0<=y<n):
                return 1
            if move==0:
                return 0
            if dp[move][x][y] != -1:
                return dp[move][x][y]
            dp[move][x][y] = 0
            for dx, dy in dirn:
                dp[move][x][y] = (dp[move][x][y] + rec(move-1, x+dx, y+dy))%mod
            dp[move][x][y] %= mod
            return dp[move][x][y]
        return rec(maxMove, startRow, startColumn)