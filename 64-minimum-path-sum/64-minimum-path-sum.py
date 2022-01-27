class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        t = [[inf]*(n+1) for _ in range(m+1)]
        t[m][n-1] = t[m-1][n] = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                t[i][j] = min(t[i][j+1], t[i+1][j]) + grid[i][j]
        return t[0][0]