class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        c = 1
        for i in range(0, (n+1)//2):
            for j in range(i, n-i):
                ans[i][j] = c
                c += 1
            for j in range(i+1, n-i):
                ans[j][n-i-1] = c
                c += 1
            for j in range(n-i-2, i-1, -1):
                ans[n-i-1][j] = c
                c += 1
            for j in range(n-i-2, i, -1):
                ans[j][i] = c
                c += 1
        return ans
            