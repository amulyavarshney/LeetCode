class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        t = [[0]*n for _ in range(m)]
        x = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    t[i][j] = min(t[i-1][j], t[i-1][j-1], t[i][j-1]) + 1
                    x = max(x, t[i][j])
        return x*x