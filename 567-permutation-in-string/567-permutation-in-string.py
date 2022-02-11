class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        d, d2 = {}, {}
        for i in range(m):
            d[s1[i]] = d.get(s1[i],0)+1
            d2[s2[i]] = d2.get(s2[i],0)+1
        for i in range(m, n):
            if d == d2:
                return True
            if d2[s2[i-m]] == 1:
                del d2[s2[i-m]]
            else:
                d2[s2[i-m]] -= 1
            d2[s2[i]] = d2.get(s2[i],0)+1
        return d == d2