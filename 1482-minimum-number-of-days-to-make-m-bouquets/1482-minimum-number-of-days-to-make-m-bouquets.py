class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(m*k > len(bloomDay)): return -1
        l, r = 1, max(bloomDay)
        while(l<=r):
            mid = l+(r-l)//2
            c, s = 0, 0
            for x in bloomDay:
                if x<=mid:
                    s += 1
                elif s>=k:
                    c += s//k
                    s = 0
                else:
                    s = 0
            if s>=k:
                c += s//k
            if c >= m:
                r = mid-1
            else:
                l = mid+1
        return r+1