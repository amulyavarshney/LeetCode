class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*(i+1) for i in range(query_row+2)]
        dp[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                flow = (dp[i][j]-1)/2
                if flow > 0:
                    dp[i+1][j] += flow
                    dp[i+1][j+1] += flow
        return min(dp[query_row][query_glass],1)