class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        q = collections.deque()
        dis = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dis[i][j] = float("inf")
                elif grid[i][j] == 2:
                    q.append((i,j))
        while q:
            i, j = q.popleft()
            for dx, dy in d:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n:
                    if dis[x][y] > dis[i][j]+1:
                        dis[x][y] = dis[i][j]+1
                        q.append((x,y))
        ans = 0
        for i in range(m):
            for j in range(n):
                    ans = max(ans, dis[i][j])
        return ans if ans != float("inf") else -1