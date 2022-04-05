class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        d = [(0,1), (1,0), (-1,0), (0,-1)]
        vis = [[False]*m for i in range(n)]
        def dfs(i,j):
            vis[i][j] = True
            for dx,dy in d:
                x, y = i+dx, j+dy
                if 0<=x<n and 0<=y<m and grid[x][y]=='1' and vis[x][y]==False:
                    dfs(x,y)
                    
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and vis[i][j]==False:
                    c += 1
                    dfs(i,j)
        return c