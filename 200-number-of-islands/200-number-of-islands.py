class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        d = [(0,1), (1,0), (-1,0), (0,-1)]
        vis = [[False]*m for i in range(n)]
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and vis[i][j]==False:
                    c += 1
                    stack = [(i,j)]
                    while len(stack)>0:
                        x, y = stack.pop()
                        vis[x][y] = True
                        for dx,dy in d:
                            xx, yy = x+dx, y+dy
                            if 0<=xx<n and 0<=yy<m and grid[xx][yy]=='1' and vis[xx][yy]==False:
                                stack.append((xx,yy))
        return c