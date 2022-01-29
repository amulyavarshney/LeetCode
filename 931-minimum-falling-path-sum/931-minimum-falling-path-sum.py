class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(m):
                matrix[i][j] = min(matrix[i-1][max(j-1, 0)], matrix[i-1][j], matrix[i-1][min(j+1, m-1)]) + matrix[i][j]
        return min(matrix[n-1])