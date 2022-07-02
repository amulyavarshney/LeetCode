class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l, r = 1, 10**7
        if len(dist)-1+dist[-1]/r > hour:
            return -1
        while(l<=r):
            m = l+(r-l)//2
            t = 0
            for i in range(len(dist)-1):
                t += (dist[i]+m-1)//m
            t += dist[-1]/m
            if t <= hour:
                r = m-1
            else:
                l = m+1
        return r+1