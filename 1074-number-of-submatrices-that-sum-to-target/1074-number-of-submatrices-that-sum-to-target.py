class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]
        count = 0
        for i in range(n):
            for j in range(i, n):
                d = {0:1}
                sums = 0
                for k in range(m):
                    sums += matrix[k][j]-(matrix[k][i-1] if i>0 else 0)
                    count += d.get(sums - target, 0)
                    d[sums] = d.get(sums, 0) + 1
        return count