class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while n not in d:
            s = 0
            d.add(n)
            while n>0:
                n, r = divmod(n, 10)
                s += r*r
            if s==1:
                return True
            n = s
        return False