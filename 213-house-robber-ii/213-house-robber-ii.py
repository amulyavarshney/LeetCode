class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # Since the first house and the last house can't be both robbed, so we have rob(nums) = max(rob(nums[1:], nums[:-1]). 
        n = len(nums)-1
        rob, notrob = 0, 0
        for i in range(1, n+1):
            rob, notrob = notrob+nums[i-1], max(rob, notrob)
        t1 = max(rob, notrob)
        rob, notrob = 0, 0
        for i in range(1, n+1):
            rob, notrob = notrob+nums[i], max(rob, notrob)
        t2 = max(rob, notrob)
        return max(t1, t2)