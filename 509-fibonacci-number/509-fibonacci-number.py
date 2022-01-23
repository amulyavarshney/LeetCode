class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        t = [0]*(n+1)
        t[1] = 1
        for i in range(2, n+1):
            t[i] = t[i-2] + t[i-1]
        return t[n]