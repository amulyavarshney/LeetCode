class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        new_grid = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r, c = divmod(i*n+j+k, n)
                new_grid[r%m][c%n] = grid[i][j]
        return new_grid