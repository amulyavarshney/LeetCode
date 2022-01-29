class Solution:
    def nthUglyNumber(self, n: int) -> int:
        t = [1]*n
        c2, c3, c5 = 0, 0, 0
        for i in range(1,n):
            p2 = 2*t[c2]
            p3 = 3*t[c3]
            p5 = 5*t[c5]
            t[i] = min(p2, p3, p5)
            if t[i] == p2:
                c2 += 1
            if t[i] == p3:
                c3 += 1
            if t[i] == p5:
                c5 += 1
        return t[-1]