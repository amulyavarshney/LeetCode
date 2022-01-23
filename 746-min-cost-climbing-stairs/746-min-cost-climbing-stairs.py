class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        n = len(cost)
        t = [0]*(n+1)
        t[1] = cost[0]
        for i in range(2, n+1):
            t[i] = min(t[i-1], t[i-2]) + cost[i-1]
        return t[n]