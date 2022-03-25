class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        c = 0
        while n>0:
            n, r = divmod(n, 3)
            c += r
        return c==1