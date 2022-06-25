class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 0, position[-1]-position[0]
        while(l<=r):
            mid = l+(r-l)//2
            x = position[0]
            c = 1
            for p in position:
                if p-x >= mid:
                    c += 1
                    x = p
            if c >= m:
                l = mid+1
            else:
                r = mid-1
        return l-1