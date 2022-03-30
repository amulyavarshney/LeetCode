class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j, m, n = 0, 0, len(matrix), len(matrix[0])
        ans = []
        while i<m and j<n:
            for r in range(j, n):
                ans.append(matrix[i][r])
            i += 1
            for c in range(i, m):
                ans.append(matrix[c][n-1])
            n -= 1
            if i<m:
                for r in range(n-1, j-1, -1):
                    ans.append(matrix[m-1][r])
            m -= 1
            if j<n:
                for c in range(m-1, i-1, -1):
                    ans.append(matrix[c][j])
            j += 1
        return ans