class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = float("inf")
        ans = -1
        for i,p in enumerate(points):
            if x == p[0] and res > abs(y-p[1]):
                res = abs(y-p[1])
                ans = i
            elif y == p[1] and res > abs(x-p[0]):
                res = abs(x-p[0])
                ans = i
        return ans