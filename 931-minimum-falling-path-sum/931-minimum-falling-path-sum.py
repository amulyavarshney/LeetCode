class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        dp[0] = matrix[0]
        for i in range(1, n):
            for j in range(m):
                dp[i][j] = min(dp[i-1][max(j-1, 0)], dp[i-1][j], dp[i-1][min(j+1, m-1)]) + matrix[i][j]
        return min(dp[n-1])