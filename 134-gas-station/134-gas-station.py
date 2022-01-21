class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g, start = 0, 0
        for i in range(len(gas)):
            g += gas[i]-cost[i]
            if g<0:
                g = 0
                start = i+1
        return start if sum(gas) >= sum(cost) else -1