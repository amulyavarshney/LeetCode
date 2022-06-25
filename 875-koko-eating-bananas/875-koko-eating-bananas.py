class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = (sum(piles)+h-1)//h, max(piles)
        while(l<r):
            mid = l + (r-l)//2
            s = 0
            for x in piles:
                s += (x+mid-1)//mid
            if s <= h:
                r = mid
            else:
                l = mid+1
        return l