class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
        while d:
            x, y = min(d, key=d.get)  # obtain the current minimum edge
            res += d.pop((x, y))      # and remove the corresponding point
            for x1, y1 in d:          # for the rest of the points, update the minimum manhattan distance
                d[(x1, y1)] = min(d[(x1, y1)], abs(x-x1)+abs(y-y1))
        return res
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         ans = 0
#         stack = set()
#         dis = [float("inf")]*n
#         dis[0] = 0
#         while len(stack)<n:
#             m = float("inf")
#             x = -1
#             for i in range(n):
#                 if i in stack:
#                     continue
#                 if m > abs()