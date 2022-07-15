class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False]*n for _ in range(m)]
        dirn = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(u, v):
            vis[u][v] = True
            count = 1
            for dx, dy in dirn:
                x, y = u+dx, v+dy
                if 0<=x<m and 0<=y<n and grid[x][y]==1 and vis[x][y]==False:
                    count += dfs(x, y)
            return count
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and vis[i][j]==False:
                    ans = max(ans, dfs(i, j))
        return ans