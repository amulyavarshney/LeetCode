class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        mini = float("inf")
        for i in range(m):
            for j in range(n):
                mini = min(mini, grid[i][j])
        for i in range(m):
            for j in range(n):
                grid[i][j] -= mini
        for i in range(m):
            for j in range(n):
                r, c = divmod(i*n+j+k, n)
                grid[r%m][c%n] = (grid[i][j]%2001)*2001 + grid[r%m][c%n]%2001
        for i in range(m):
            for j in range(n):
                grid[i][j] //= 2001
                grid[i][j] += mini
        return grid