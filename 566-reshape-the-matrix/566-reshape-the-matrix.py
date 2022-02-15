class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        ans = [[0]*c for _ in range(r)]
        for i in range(m*n):
            x, y = divmod(i, n)
            a, b = divmod(i, c)
            ans[a][b] = mat[x][y]
        return ans