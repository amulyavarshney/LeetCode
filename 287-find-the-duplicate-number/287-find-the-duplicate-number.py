class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            if x in d:
                return x
            d[x] = 1