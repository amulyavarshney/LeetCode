class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        t = [[0]*(m+1) for _ in range(n+1)]
        def lcs(x, y, n, m):
            for i in range(n+1):
                t[i][0] = i
            for j in range(m+1):
                t[0][j] = j
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if x[i-1] == y[j-1]:
                        t[i][j] = t[i-1][j-1]
                    else:
                        t[i][j] = min(t[i-1][j-1], t[i][j-1], t[i-1][j]) + 1
            return t[n][m]
        return lcs(word1, word2, n, m)