class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for x in nums:
            p*=x
        return 1 if p>0 else -1 if p<0 else 0