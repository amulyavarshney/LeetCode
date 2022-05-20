class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        t = [[0]*n for _ in range(m)]
        f = 1
        for i in range(m):
            if grid[i][0] == 1:
                f = 0
            t[i][0] = f
        f = 1
        for j in range(n):
            if grid[0][j] == 1:
                f = 0
            t[0][j] = f
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    t[i][j] = t[i][j-1] + t[i-1][j]
                else:
                    t[i][j] = 0
        return t[m-1][n-1]