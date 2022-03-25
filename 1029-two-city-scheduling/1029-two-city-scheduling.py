class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s = sum(x[0] for x in costs)
        refund = sorted([x[1]-x[0] for x in costs])
        for i in range(len(costs)//2):
            s += refund[i]
        return s