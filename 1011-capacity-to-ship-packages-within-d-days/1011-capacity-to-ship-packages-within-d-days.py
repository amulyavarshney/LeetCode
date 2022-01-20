class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = 0
        while l<=r:
            m = l + (r-l)//2
            s, c = 0, 0
            for x in weights:
                if s+x > m:
                    s = x
                    c += 1
                else:
                    s += x
            if c+1 <= days:
                ans = m
                r = m-1
            else:
                l = m+1
        return ans