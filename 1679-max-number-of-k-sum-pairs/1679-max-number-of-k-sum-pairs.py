class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = 0
        d = {}
        for x in nums:
            if d.get(k-x, 0) > 0:
                c += 1
                d[k-x] -= 1
            else:
                d[x] = d.get(x, 0) + 1
        return c