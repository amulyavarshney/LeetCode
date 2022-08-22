class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        c = 0
        while n>0:
            n, r = divmod(n, 4)
            c += r
        return c==1