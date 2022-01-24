class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        avoid, using = 0, 0
        p = -1
        for k in sorted(d):
            if p+1 == k:
                avoid, using = max(avoid, using), avoid+k*d[k]
            else:
                avoid, using = max(avoid, using), max(avoid, using)+k*d[k]
            p = k
        return max(avoid, using)