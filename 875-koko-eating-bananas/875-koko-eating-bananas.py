class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, n = sum(piles), len(piles)
        l, r = (s+h-1)//h, s
        ans = 0
        while l<=r:
            m = l + (r-l)//2
            x = 0
            for i in range(n):
                x += (piles[i]+m-1)//m
            if x <= h:
                ans = m
                r = m-1
            else:
                l = m+1
        return ans